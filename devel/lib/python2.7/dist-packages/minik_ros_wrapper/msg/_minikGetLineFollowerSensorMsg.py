# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from minik_ros_wrapper/minikGetLineFollowerSensorMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class minikGetLineFollowerSensorMsg(genpy.Message):
  _md5sum = "117f4dd679610c07fd2b537377a09014"
  _type = "minik_ros_wrapper/minikGetLineFollowerSensorMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Minik Get Line Follower Message

char rightSensor
char middleSensor
char leftSensor
"""
  __slots__ = ['rightSensor','middleSensor','leftSensor']
  _slot_types = ['char','char','char']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       rightSensor,middleSensor,leftSensor

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(minikGetLineFollowerSensorMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.rightSensor is None:
        self.rightSensor = 0
      if self.middleSensor is None:
        self.middleSensor = 0
      if self.leftSensor is None:
        self.leftSensor = 0
    else:
      self.rightSensor = 0
      self.middleSensor = 0
      self.leftSensor = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3B().pack(_x.rightSensor, _x.middleSensor, _x.leftSensor))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 3
      (_x.rightSensor, _x.middleSensor, _x.leftSensor,) = _get_struct_3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3B().pack(_x.rightSensor, _x.middleSensor, _x.leftSensor))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 3
      (_x.rightSensor, _x.middleSensor, _x.leftSensor,) = _get_struct_3B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
