
 - [安装pygame](#%E5%AE%89%E8%A3%85pygame)
  - [安装pygame](#%E5%AE%89%E8%A3%85pygame)
- [安装pygame](#%E5%AE%89%E8%A3%85pygame)
- [pygame 基本模块](#pygame-%E5%9F%BA%E6%9C%AC%E6%A8%A1%E5%9D%97)
- [pygame 基本导入](#pygame-%E5%9F%BA%E6%9C%AC%E5%AF%BC%E5%85%A5)
- [基本窗口属性](#%E5%9F%BA%E6%9C%AC%E7%AA%97%E5%8F%A3%E5%B1%9E%E6%80%A7)
- [事件](#%E4%BA%8B%E4%BB%B6)

# 安装pygame
pip install pygame
还需要安装轮子,下载文件 pygame-1.9.3-cp36-cp36m-win_amd64.whl
pip install pygame-1.9.3-cp36-cp36m-win_amd64.whl

# pygame 基本模块
| 模块名           | 功能                        |
| ---------------- | --------------------------- |
| pygame.cdrom     | 访问光驱                    |
| pygame.cursors   | 加载光标                    |
| pygame.display   | 访问显示设备                |
| pygame.draw      | 绘制形状、线和点            |
| pygame.event     | 管理事件                    |
| pygame.font      | 使用字体                    |
| pygame.image     | 加载和存储图片              |
| pygame.joystick  | 使用游戏手柄或者 类似的东西 |
| pygame.key       | 读取键盘按键                |
| pygame.mixe      | 声音                        |
| pygame.mouse     | 鼠标                        |
| pygame.movie     | 播放视频                    |
| pygame.music     | 播放音频                    |
| pygame.overlay   | 访问高级视频叠加            |
| pygame           | 就是我们在学的这个东西了……  |
| pygame.rect      | 管理矩形区域                |
| pygame.sndarray  | 操作声音数据                |
| pygame.sprite    | 操作移动图像                |
| pygame.surface   | 管理图像和屏幕              |
| pygame.surfarray | 管理点阵图像数据            |
| pygame.time      | 管理时间和帧信息            |
| pygame.transform | 缩放和移动图像              |


# pygame 基本导入

  import pygame
  #导入pygame库
  from pygame.locals import *
  #导入一些常用的函数和常量
  from sys import exit
  #向sys模块借一个exit函数用来退出程序
  pygame.init()


# 基本窗口属性

```python
screen = pygame.display.set_mode((640, 480), 0, 32)
screen.blit(background, (0,0))
```

|标志位|功能|
|--|--|
|0||
|FULLSCREEN|创建一个全屏窗口|
|DOUBLEBUF|创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用|
|HWSURFACE|创建一个硬件加速的窗口，必须和FULLSCREEN同时使用|
|OPENGL|创建一个OPENGL渲染的窗口|
|RESIZABLE|创建一个可以改变大小的窗口|
|NOFRAME|创建一个没有边框的窗口|

# 事件
事件检索
pygame.event.get()   来处理所有的事件
pygame.event.wait()  Pygame就会等到发生一个事件才继续下去
pygame.event.poll()  一旦调用，它会根据现在的情形返回一个真实的事件，或者一个“什么都没有”

常用事件

|事件|产生途径|参数|
|-|-|-|
|QUIT|用户按下关闭按钮|none|
|ATIVEEVENT|Pygame被激活或者隐藏|gain, state|
|KEYDOWN|键盘被按下|unicode, key, mod|
|KEYUP|键盘被放开|key, mod|
|MOUSEMOTION|鼠标移动|pos, rel, buttons|
|MOUSEBUTTONDOWN|鼠标按下|pos, button|
|MOUSEBUTTONUP|鼠标放开|pos, button|
|JOYAXISMOTION|游戏手柄(Joystick or pad)移动|joy, axis, value|
|JOYBALLMOTION|游戏球(Joy ball)?移动|joy, axis, value|
|JOYHATMOTION|游戏手柄(Joystick)?移动|joy, axis, value|
|JOYBUTTONDOWN|游戏手柄按下|joy, button|
|JOYBUTTONUP|游戏手柄放开|joy, button|
|VIDEORESIZE|Pygame窗口缩放|size, w, h|
|VIDEOEXPOSE|Pygame窗口部分公开(expose)?|none|
|USEREVENT|触发了一个用户事件|code|