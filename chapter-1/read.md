*******
bool(x)的背后是调用x.__bool__()的结果,
如果不存在__bool__方法，那么bool(x)会尝试
调用x.__len__()根据返回长度判断布尔值
*******
