from bson import ObjectId
from dateutil import parser


class ModelGet(object):
    def __init__(self, **kwargs):
        self._id = str(kwargs.get("_id"))
        self.pack = kwargs.get("pack")
        self.module = kwargs.get("module")
        self.objectType = kwargs.get("objectType")
        self.action = kwargs.get("action")
        self.logs = kwargs.get("logs")
        self.oldData = kwargs.get("oldData")
        self.newData = kwargs.get("newData")
        self.user = kwargs.get("user")
        self.viewType = kwargs.get("viewType")
        self.target = kwargs.get("target")
        self.creatorId = kwargs.get("creatorId")
        self.creatorIp = kwargs.get("creatorIp")
        self.created = str(kwargs.get("created"))
        self.editorId = kwargs.get("editorId")
        self.editorIp = kwargs.get("editorIp")
        self.lastModified = str(kwargs.get("lastModified"))
        self.isDelete = kwargs.get("isDelete")
        self.deleted = kwargs.get("deleted")


class ModelInsert(object):
    def __init__(self, **kwargs):
        self._id = ObjectId(kwargs.get("_id"))
        self.id = ObjectId(kwargs.get("_id"))
        self.pack = kwargs.get("pack")
        self.module = kwargs.get("module")
        self.objectType = kwargs.get("objectType")
        self.action = kwargs.get("action")
        self.logs = kwargs.get("logs")
        self.oldData = kwargs.get("oldData")
        self.newData = kwargs.get("newData")
        self.user = kwargs.get("user")
        self.viewType = kwargs.get("viewType")
        self.target = kwargs.get("target")
        self.creatorId = kwargs.get("creatorId")
        self.creatorIp = kwargs.get("creatorIp")
        self.created = parser.parse(kwargs.get("created"))
        self.editorId = kwargs.get("editorId")
        self.editorIp = kwargs.get("editorIp")
        self.lastModified = parser.parse(kwargs.get("lastModified"))
        self.isDelete = kwargs.get("isDelete")
        self.deleted = kwargs.get("deleted")