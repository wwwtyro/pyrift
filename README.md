pyrift
======

Python wrapper for the Oculus Rift SDK

```python
>>> import pyrift
>>> pyrift.initialize()
>>> pyrift.get_orientation()
(-0.0001147584043792449, 0.27211394906044006, -0.006657531019300222)
>>> pyrift.is_calibrated()
False
>>> # The rift is rotated through a range of orientations.
... 
>>> pyrift.is_calibrated()
True
```
