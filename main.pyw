#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import navigator_widget
import sys, urllib.request, urllib.parse, json, subprocess, os, os.path
from math import *



class AppMainWindow(QMainWindow):
	
	def __init__(self):
		QMainWindow.__init__(self)
		self.model=None
		self.ui=None
		self.query=Query(self)
		self.query.changed.connect(self.queryChanged)
		self.baseUrl='http://localhost:8000'
		
	def setUi(self,ui):
		self.ui=ui
		#data=self.post('/find/',{'limit':100,'tagCloud':True,'tagCloudLimit':50,'tags':[]},2.0)
		self.ui.graphicsView.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate);
		self.ui.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
		self.ui.graphicsView.setMouseTracking(True)
		self.scene=TagCloudScene()
		self.ui.graphicsView.setScene(self.scene)
		self.ui.graphicsView.setCursor(Qt.PointingHandCursor)
		
		self.queryModel=QueryTableModel(self)
		self.ui.queryTable.setModel(self.queryModel)
		self.ui.queryTable.horizontalHeader().setStretchLastSection(True)
		self.ui.queryTable.setColumnWidth(0,24)
		self.ui.queryTable.clicked.connect(self.queryItemClicked)

		self.scene.tagClicked.connect(self.addTag)
		
		self.resourceModel=ResourceTableModel(self,self.ui.resourceTable)
		
		completer = QCompleter([], self.ui.searchBox)
		completer.setCompletionColumn(0)
		completer.setMaxVisibleItems(20)
		completer.setCompletionRole(Qt.EditRole)
		completer.setCaseSensitivity(Qt.CaseInsensitive)
		completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
		self.searchCompleter=completer
		self.ui.searchBox.setCompleter(completer)
		
		self.ui.searchBox.textEdited.connect(self.searchTextChanged)
		self.ui.searchBox.returnPressed.connect(self.addSearchBox)
		self.ui.homeButton.clicked.connect(self.home)
		
		
		self.home()

	def searchTextChanged(self,s):
		data=self.getSuggestions(s)
		l=[]
		for i in data:
			l.append(i[0])
		model=self.searchCompleter.model()
		model.setStringList(l)

	def getSuggestions(self,s):
		return self.post('/suggestions/',{'prefix':s,'limit':20,'exclude':[]},0.2)

	def addSearchBox(self):
		tag=self.ui.searchBox.text()
		QTimer.singleShot(200,self.ui.searchBox.clear)
		self.addTag(tag)
		
	def home(self):
		self.query.clear()
		self.ui.searchBox.setFocus()

	def queryItemClicked(self,idx):
		if idx.column()==0:
			self.query.removeTag(idx.row())

	def addTag(self,tag):
		self.query.addTag(tag)
		
	def queryChanged(self):
		data=self.query.query()
		if data and 'tagCloud' in data:
			self.scene.reinit(data['tagCloud'])
		if len(self.query.tags):
			count=0
			if data and 'resources' in data:
				self.resourceModel.reset(data['resources'])
				count=len(data['resources'])
			else:
				count=0
				self.resourceModel.reset([])
			self.ui.resourceLabel.setText('Resources ('+str(count)+')')
		else:
			self.resourceModel.reset([])
			self.ui.resourceLabel.setText('Resources')
			
		self.queryModel.reinit()

	def deleteResource(self,res):
		msgBox = QMessageBox()
		msgBox.setText('<h1>Deleting resource</h1>')
		msgBox.setInformativeText(self.tr('Are yu sure you want to delete')+' "'+res['label']+'"?')
		msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msgBox.setDefaultButton(QMessageBox.No)
		msgBox.setIcon(QMessageBox.Warning)
		ret = msgBox.exec_()
		if ret==QMessageBox.Yes:
			self.post('/remove/',{'url':res['_url']},2.0)
			self.queryChanged()


	def post(self,addr,data,to=2.0):
		body=json.dumps(data).encode('utf-8')
		addr=self.baseUrl+addr
		conn = urllib.request.urlopen(addr,body,timeout=to)
		r=conn.read().decode('utf-8')
		conn.close()
		r=json.loads(r)
		return r
			
			
class Query(QObject):
	
	changed=Signal()
	
	def __init__(self,app):
		QObject.__init__(self)
		self.app=app
		self.tags=[]
		
	def addTag(self,name):
		self.tags.append(name)
		self.changed.emit()
		
	def query(self):
		return self.app.post('/find/',{'limit':100,'tagCloud':True,'tagCloudLimit':50,'tags':self.tags,'orderBy':'label'},2.0)

	def removeTag(self,tagIdx):
		del self.tags[tagIdx]
		self.changed.emit()
		
	def getTags(self):
		return self.tags
		
	def getTag(self,idx):
		return self.tags[idx]
		
	def clear(self):
		self.tags=[]
		self.changed.emit()
		
			
class ResourceListItem(QListWidgetItem):
	
	def __init__(self,res):
		self.res=res
		QListWidgetItem.__init__(self,res['label'])
		
	def getResource(self):
			return self.res


class TagCloudScene(QGraphicsScene):
	
	tagClicked=Signal(str)
	
	def mousePressEvent(self,e):
		i=self.itemAt(e.scenePos())
		if i:
			self.tagClicked.emit(i.toPlainText())
	
	def reinit(self,tags):
		
		self.clear()
		if not len(tags):
			return
		
		tags.sort(key=lambda x: x['name'].lower())
		
		
		minw=None
		maxw=None
		for tag in tags:
			if minw is None or tag['weight']<minw:
				minw=tag['weight']
			if maxw is None or tag['weight']>maxw:
				maxw=tag['weight']
		maxw=maxw+0.5
		minw=minw-0.5
		area=0
		maxwidth=0
		items=[]
		for tag in tags:
			text=QGraphicsTextItem()
			text.setPlainText(tag['name'])
			rw=(tag['weight']-minw)*1.0/(maxw-minw)
			font=QFont('Sans',8.0+15.0*rw)
			text.setFont(font)
			if rw<0.5:
				f=rw*2
				red=int(180)
				green=int(180-75*f)
				blue=int(180+75*f)
			else:
				f=(rw-0.5)*2
				red=int(180-180*f)
				green=int(110+145*f)
				blue=int(255-255*f)
			text.setDefaultTextColor(QColor(red,green,blue,255))
			items.append(text)
			rect=text.boundingRect()
			area=area+rect.width()*rect.height()
			if rect.width()>maxwidth:
				maxwidth=rect.width()
			
		width=sqrt(area*1.5)
		if width>300:
			width=300
		if width<maxwidth:
			width=maxwidth
		
		top=0.0
		left=0.0
		maxh=0.0
		lineitems=[]
		for text in items:
			rect=text.boundingRect()
			if left+rect.width()>width:
				# new line
				for item in lineitems:
					item['i'].setPos(item['l'],top+(maxh-item['h'])/2.0)
					self.addItem(item['i'])
					'''
					gr=QGraphicsRectItem(item['i'].boundingRect())
					gr.setPos(item['l'],top+(maxh-item['h'])/2.0)
					self.scene.addItem(gr)
					'''
				lineitems=[]
				top=top+maxh
				maxh=0.0
				left=0.0
			lineitems.append({'i':text,'l':left,'h':rect.height()})
			left=left+rect.width()
			if rect.height()>maxh:
				maxh=rect.height()
		
		for item in lineitems:
			item['i'].setPos(item['l'],top+(maxh-item['h']))
			self.addItem(item['i'])
		
		#rect=self.scene.itemsBoundingRect()
		#self.ui.graphicsView.fitInView(rect)
		
	
	
class QueryTableModel(QAbstractTableModel):
	
	def __init__(self,app):
		self.app=app
		QAbstractTableModel.__init__(self)
		
	def rowCount(self,parent):
		return len(self.app.query.getTags())
	
	def columnCount(self,parent):
		return 2
	
	def data(self, index, role):
		if not index.isValid():
			return 
		if index.column()==0:
			if role==Qt.DisplayRole:
				return 'x'
		elif index.column()==1:
			if role==Qt.DisplayRole:
				return self.app.query.getTag(index.row())
			
	def reinit(self):
		self.layoutAboutToBeChanged.emit()
		self.layoutChanged.emit()



class ResourceTableModel:

	COL_RESOURCE=2
	COL_DIRECTORY=1
	COL_TAGME=0
	COL_DELETE=3

	NotExistsBrush=QBrush(QColor(255,0,0,255))
	NormalBrush=QBrush(QColor(0,0,0,255))


	def __init__(self,app,view):
		self.app=app
		self.view=view
		self.view.doubleClicked.connect(self.tableDoubleClicked)
		self.resources=[]
		
	def deleteResource(self,res):
		self.app.deleteResource(res)
		
	def reset(self,resources):
		self.resources=resources
		self.reinit()
		
	def openResource(self,res):
		filename=res['_url']
		self.launchFile(filename)
		
	def launchFile(self,filename):
		if sys.platform == "win32":
			os.startfile(filename)
		else:
			opener ="open" if sys.platform == "darwin" else "xdg-open"
			subprocess.call([opener, filename])

	def tableDoubleClicked(self,idx):
		if idx.column()==self.COL_RESOURCE:
			self.openResource(self.resources[idx.row()])

	def getDirectory(self,res):
		if res['_url'][:7]=='file://':
			steps=urllib.parse.unquote(res['_url'][7:]).split('/')
			if steps[-1]=='':
				steps=steps[:-2]
			else:
				steps=steps[:-1]
			d='/'.join(steps)
			if os.path.exists(d):
				return d
	
	def fileExists(self,res):
		if res['_url'][:7]=='file://':
			fpath=urllib.parse.unquote(res['_url'][7:])
			return os.path.exists(fpath)
		else:
			return True
	
			
	def reinit(self):
		self.view.clear()
		self.view.setColumnCount(4)
		self.view.setRowCount(len(self.resources))
		self.view.setColumnWidth(self.COL_DIRECTORY,40)
		self.view.setColumnWidth(self.COL_TAGME,40)
		self.view.setColumnWidth(self.COL_DELETE,40)
		hh=self.view.horizontalHeader()
		hh.setResizeMode(self.COL_RESOURCE,QHeaderView.Stretch)
		hh.setResizeMode(self.COL_DIRECTORY,QHeaderView.Fixed)
		hh.setResizeMode(self.COL_TAGME,QHeaderView.Fixed)
		hh.setResizeMode(self.COL_DELETE,QHeaderView.Fixed)
		i=0
		for res in self.resources:
			label=QLabel(res['label'])
			if i%2:
				style='background-color: #FFFFDD; '
			else:
				style='background-color: #FFFFFF; '
			style=style+'padding-left: 5px; '
			if not self.fileExists(res):
				style=style+'color: #FF0000;'
			label.setStyleSheet(style)
			label.setCursor(Qt.PointingHandCursor)
			self.view.setCellWidget(i,self.COL_RESOURCE,label)
			
			d=self.getDirectory(res)
			if d:
				self.view.setCellWidget(i,self.COL_DIRECTORY,DirectoryButton(self,res))

			self.view.setCellWidget(i,self.COL_TAGME,TaggerButton(self,res))

			self.view.setCellWidget(i,self.COL_DELETE,DeleteButton(self,res))

			i=i+1
			
		#self.view.setAlternatingRowColors(True)
		#self.view.setStyleSheet('alternate-background-color: yellow; background-color: white;')

	def openDirectory(self,res):
		d=self.getDirectory(res)
		if d:
			self.launchFile(d)

class DirectoryButton(QPushButton):
	
	def __init__(self,model,res):
		self.res=res
		self.model=model
		QPushButton.__init__(self)
		ico=QPixmap(":/dedalus/directory.png")
		self.setIcon(ico)
		self.setIconSize(ico.rect().size())
		self.clicked.connect(self.openDirectory)
		
	def openDirectory(self):
		self.model.openDirectory(self.res)

class TaggerButton(QPushButton):
	
	def __init__(self,model,res):
		self.res=res
		self.model=model
		QPushButton.__init__(self)
		ico=QPixmap(":/dedalus/tagme.png")
		self.setIcon(ico)
		self.setIconSize(ico.rect().size())
		self.clicked.connect(self.openTagger)
		
	def openTagger(self):
		os.system('dedalus-tagger "'+self.res['_url']+'"')

class DeleteButton(QPushButton):
	
	def __init__(self,model,res):
		self.res=res
		self.model=model
		QPushButton.__init__(self)
		ico=QPixmap(":/dedalus/delete.png")
		self.setIcon(ico)
		self.setIconSize(ico.rect().size())
		self.clicked.connect(self.deleteResource)
		
	def deleteResource(self):
		self.model.deleteResource(self.res)



def main():
	app = QApplication(sys.argv)
	ui = navigator_widget.Ui_MainWindow()
	mainWindow = AppMainWindow()
	ui.setupUi(mainWindow)
	mainWindow.setUi(ui)
	mainWindow.show()
	app.exec_()
	sys.exit()
if __name__ == "__main__":
	main()

