# colorbox

Color box that provides various colors‘ rgb decimal code.

## Usage

```python
>>> from colorbox import rgb, bgr, hex
>>> rgb("red")
(255, 0, 0)
>>> bgr("red")
(0, 0, 255)
>>> hex("red")
'#FF0000'
```

## Color Map

来源： <https://www.rapidtables.com/web/color/RGB_Color.html>

推荐安装 vscode 插件 Color Highlight 更直观地查看以下颜色

|                                                            | Hex Code#RRGGBB | Decimal CodeR,G,B |         en_name         | zh_name       |
| ---------------------------------------------------------- | :-------------: | :---------------: | :---------------------: | ------------- |
| <span style="background-color:#FF0000">&emsp;&emsp;</span> |     #FF0000     |     (255,0,0)     |           red           | 红色          |
| <span style="background-color:#FFA500">&emsp;&emsp;</span> |     #FFA500     |    (255,165,0)    |         orange          | 橙色          |
| <span style="background-color:#FFFF00">&emsp;&emsp;</span> |     #FFFF00     |    (255,255,0)    |         yellow          | 黄色          |
| <span style="background-color:#008000">&emsp;&emsp;</span> |     #008000     |     (0,128,0)     |          green          | 绿色          |
| <span style="background-color:#00FFFF">&emsp;&emsp;</span> |     #00FFFF     |    (0,255,255)    |        cyan/aqua        | 青色/水色     |
| <span style="background-color:#0000FF">&emsp;&emsp;</span> |     #0000FF     |     (0,0,255)     |          blue           | 蓝色          |
| <span style="background-color:#FF00FF">&emsp;&emsp;</span> |     #FF00FF     |    (255,0,255)    |     magenta/fuchsia     | 洋红色/紫红色 |
| <span style="background-color:#7FFFD4">&emsp;&emsp;</span> |     #7FFFD4     |   (127,255,212)   |       aqua marine       | 海洋蓝        |
| <span style="background-color:#FF2400">&emsp;&emsp;</span> |     #FF2400     |    (255,36,0)     |         scarlet         | 猩红色        |
| <span style="background-color:#00FF00">&emsp;&emsp;</span> |     #00FF00     |     (0,255,0)     |          lime           | 酸橙绿        |
| <span style="background-color:#FFFFFF">&emsp;&emsp;</span> |     #FFFFFF     |   (255,255,255)   |          white          | 白色          |
| <span style="background-color:#C0C0C0">&emsp;&emsp;</span> |     #C0C0C0     |   (192,192,192)   |         silver          | 银色          |
| <span style="background-color:#808080">&emsp;&emsp;</span> |     #808080     |   (128,128,128)   |          gray           | 灰色          |
| <span style="background-color:#008080">&emsp;&emsp;</span> |     #008080     |    (0,128,128)    |          teal           | 青色          |
| <span style="background-color:#800000">&emsp;&emsp;</span> |     #800000     |     (128,0,0)     |         maroon          | 栗色          |
| <span style="background-color:#808000">&emsp;&emsp;</span> |     #808000     |    (128,128,0)    |          olive          | 橄榄色        |
| <span style="background-color:#800080">&emsp;&emsp;</span> |     #800080     |    (128,0,128)    |         purple          | 紫色          |
| <span style="background-color:#000080">&emsp;&emsp;</span> |     #000080     |     (0,0,128)     |          navy           | 海军色        |
| <span style="background-color:#FFD700">&emsp;&emsp;</span> |     #FFD700     |    (255,215,0)    |          gold           | 金色          |
| <span style="background-color:#B8860B">&emsp;&emsp;</span> |     #B8860B     |   (184,134,11)    |     dark golden rod     | 暗金棒        |
| <span style="background-color:#DAA520">&emsp;&emsp;</span> |     #DAA520     |   (218,165,32)    |       golden rod        | 金棒          |
| <span style="background-color:#000000">&emsp;&emsp;</span> |     #000000     |      (0,0,0)      |          black          | 黑色          |
| <span style="background-color:#EEE8AA">&emsp;&emsp;</span> |     #EEE8AA     |   (238,232,170)   |     pale golden rod     | 淡金色棒      |
| <span style="background-color:#BDB76B">&emsp;&emsp;</span> |     #BDB76B     |   (189,183,107)   |       dark khaki        | 深卡其色      |
| <span style="background-color:#F0E68C">&emsp;&emsp;</span> |     #F0E68C     |   (240,230,140)   |          khaki          | 卡其色        |
| <span style="background-color:#9ACD32">&emsp;&emsp;</span> |     #9ACD32     |   (154,205,50)    |      yellow green       | 黄绿色        |
| <span style="background-color:#556B2F">&emsp;&emsp;</span> |     #556B2F     |    (85,107,47)    |    dark olive green     | 深橄榄绿      |
| <span style="background-color:#6B8E23">&emsp;&emsp;</span> |     #6B8E23     |   (107,142,35)    |       olive drab        | 橄榄色        |
| <span style="background-color:#7FFF00">&emsp;&emsp;</span> |     #7FFF00     |    (127,255,0)    |       chart reuse       | 黄绿色        |
| <span style="background-color:#ADFF2F">&emsp;&emsp;</span> |     #ADFF2F     |   (173,255,47)    |      green yellow       | 黄绿色        |
| <span style="background-color:#006400">&emsp;&emsp;</span> |     #006400     |     (0,100,0)     |       dark green        | 深绿色        |
| <span style="background-color:#228B22">&emsp;&emsp;</span> |     #228B22     |    (34,139,34)    |      forest green       | 森林绿        |
| <span style="background-color:#32CD32">&emsp;&emsp;</span> |     #32CD32     |    (50,205,50)    |       lime green        | 柠檬绿        |
| <span style="background-color:#90EE90">&emsp;&emsp;</span> |     #90EE90     |   (144,238,144)   |       light green       | 浅绿色        |
| <span style="background-color:#8FBC8F">&emsp;&emsp;</span> |     #8FBC8F     |   (143,188,143)   |     dark sea green      | 深海绿色      |
| <span style="background-color:#00FA9A">&emsp;&emsp;</span> |     #00FA9A     |    (0,250,154)    |   medium spring green   | 中春绿        |
| <span style="background-color:#00FF7F">&emsp;&emsp;</span> |     #00FF7F     |    (0,255,127)    |      spring green       | 春绿          |
| <span style="background-color:#2E8B57">&emsp;&emsp;</span> |     #2E8B57     |    (46,139,87)    |        sea green        | 海绿色        |
| <span style="background-color:#66CDAA">&emsp;&emsp;</span> |     #66CDAA     |   (102,205,170)   |   medium aqua marine    | 中型海蓝      |
| <span style="background-color:#3CB371">&emsp;&emsp;</span> |     #3CB371     |   (60,179,113)    |    medium sea green     | 中海绿        |
| <span style="background-color:#20B2AA">&emsp;&emsp;</span> |     #20B2AA     |   (32,178,170)    |     light sea green     | 浅海绿色      |
| <span style="background-color:#2F4F4F">&emsp;&emsp;</span> |     #2F4F4F     |    (47,79,79)     |     dark slate gray     | 深石板灰      |
| <span style="background-color:#008B8B">&emsp;&emsp;</span> |     #008B8B     |    (0,139,139)    |        dark cyan        | 深青色        |
| <span style="background-color:#E0FFFF">&emsp;&emsp;</span> |     #E0FFFF     |   (224,255,255)   |       light cyan        | 淡青色        |
| <span style="background-color:#00CED1">&emsp;&emsp;</span> |     #00CED1     |    (0,206,209)    |     dark turquoise      | 深绿松石      |
| <span style="background-color:#40E0D0">&emsp;&emsp;</span> |     #40E0D0     |   (64,224,208)    |        turquoise        | 绿松石        |
| <span style="background-color:#48D1CC">&emsp;&emsp;</span> |     #48D1CC     |   (72,209,204)    |    medium turquoise     | 中绿松石      |
| <span style="background-color:#AFEEEE">&emsp;&emsp;</span> |     #AFEEEE     |   (175,238,238)   |     pale turquoise      | 淡绿松石      |
| <span style="background-color:#B0E0E6">&emsp;&emsp;</span> |     #B0E0E6     |   (176,224,230)   |       powder blue       | 粉蓝色        |
| <span style="background-color:#5F9EA0">&emsp;&emsp;</span> |     #5F9EA0     |   (95,158,160)    |       cadet blue        | 学员蓝        |
| <span style="background-color:#4682B4">&emsp;&emsp;</span> |     #4682B4     |   (70,130,180)    |       steel blue        | 钢蓝色        |
| <span style="background-color:#6495ED">&emsp;&emsp;</span> |     #6495ED     |   (100,149,237)   |    corn flower blue     | 玉米花蓝色    |
| <span style="background-color:#00BFFF">&emsp;&emsp;</span> |     #00BFFF     |    (0,191,255)    |      deep sky blue      | 深蓝色        |
| <span style="background-color:#1E90FF">&emsp;&emsp;</span> |     #1E90FF     |   (30,144,255)    |       dodger blue       | 道奇蓝        |
| <span style="background-color:#ADD8E6">&emsp;&emsp;</span> |     #ADD8E6     |   (173,216,230)   |       light blue        | 浅蓝          |
| <span style="background-color:#87CEEB">&emsp;&emsp;</span> |     #87CEEB     |   (135,206,235)   |        sky blue         | 天蓝色        |
| <span style="background-color:#87CEFA">&emsp;&emsp;</span> |     #87CEFA     |   (135,206,250)   |     light sky blue      | 淡天蓝色      |
| <span style="background-color:#191970">&emsp;&emsp;</span> |     #191970     |    (25,25,112)    |      midnight blue      | 午夜蓝        |
| <span style="background-color:#00008B">&emsp;&emsp;</span> |     #00008B     |     (0,0,139)     |        dark blue        | 深蓝          |
| <span style="background-color:#0000CD">&emsp;&emsp;</span> |     #0000CD     |     (0,0,205)     |       medium blue       | 中蓝色        |
| <span style="background-color:#4169E1">&emsp;&emsp;</span> |     #4169E1     |   (65,105,225)    |       royal blue        | 宝蓝色        |
| <span style="background-color:#8A2BE2">&emsp;&emsp;</span> |     #8A2BE2     |   (138,43,226)    |       blue violet       | 紫罗兰色      |
| <span style="background-color:#4B0082">&emsp;&emsp;</span> |     #4B0082     |    (75,0,130)     |         indigo          | 靛青          |
| <span style="background-color:#483D8B">&emsp;&emsp;</span> |     #483D8B     |    (72,61,139)    |     dark slate blue     | 深石板蓝      |
| <span style="background-color:#6A5ACD">&emsp;&emsp;</span> |     #6A5ACD     |   (106,90,205)    |       slate blue        | 石板蓝        |
| <span style="background-color:#7B68EE">&emsp;&emsp;</span> |     #7B68EE     |   (123,104,238)   |    medium slate blue    | 中石板蓝      |
| <span style="background-color:#9370DB">&emsp;&emsp;</span> |     #9370DB     |   (147,112,219)   |      medium purple      | 中紫色        |
| <span style="background-color:#8B008B">&emsp;&emsp;</span> |     #8B008B     |    (139,0,139)    |      dark magenta       | 深洋红色      |
| <span style="background-color:#9400D3">&emsp;&emsp;</span> |     #9400D3     |    (148,0,211)    |       dark violet       | 深紫色        |
| <span style="background-color:#9932CC">&emsp;&emsp;</span> |     #9932CC     |   (153,50,204)    |       dark orchid       | 暗兰花        |
| <span style="background-color:#BA55D3">&emsp;&emsp;</span> |     #BA55D3     |   (186,85,211)    |      medium orchid      | 中等兰花      |
| <span style="background-color:#D8BFD8">&emsp;&emsp;</span> |     #D8BFD8     |   (216,191,216)   |         thistle         | 蓟            |
| <span style="background-color:#DDA0DD">&emsp;&emsp;</span> |     #DDA0DD     |   (221,160,221)   |          plum           | 李子          |
| <span style="background-color:#EE82EE">&emsp;&emsp;</span> |     #EE82EE     |   (238,130,238)   |         violet          | 紫色          |
| <span style="background-color:#DA70D6">&emsp;&emsp;</span> |     #DA70D6     |   (218,112,214)   |         orchid          | 兰花          |
| <span style="background-color:#C71585">&emsp;&emsp;</span> |     #C71585     |   (199,21,133)    |    medium violet red    | 中紫红色      |
| <span style="background-color:#DB7093">&emsp;&emsp;</span> |     #DB7093     |   (219,112,147)   |     pale violet red     | 淡紫红色      |
| <span style="background-color:#FF1493">&emsp;&emsp;</span> |     #FF1493     |   (255,20,147)    |        deep pink        | 深粉色        |
| <span style="background-color:#FF69B4">&emsp;&emsp;</span> |     #FF69B4     |   (255,105,180)   |        hot pink         | 亮粉色        |
| <span style="background-color:#FFB6C1">&emsp;&emsp;</span> |     #FFB6C1     |   (255,182,193)   |       light pink        | 浅粉色        |
| <span style="background-color:#FFC0CB">&emsp;&emsp;</span> |     #FFC0CB     |   (255,192,203)   |          pink           | 粉色          |
| <span style="background-color:#FAEBD7">&emsp;&emsp;</span> |     #FAEBD7     |   (250,235,215)   |      antique white      | 古色古香白色  |
| <span style="background-color:#F5F5DC">&emsp;&emsp;</span> |     #F5F5DC     |   (245,245,220)   |          beige          | 浅褐色        |
| <span style="background-color:#FFE4C4">&emsp;&emsp;</span> |     #FFE4C4     |   (255,228,196)   |         bisque          | 浓汤          |
| <span style="background-color:#FFEBCD">&emsp;&emsp;</span> |     #FFEBCD     |   (255,235,205)   |     blanched almond     | 漂白杏仁      |
| <span style="background-color:#F5DEB3">&emsp;&emsp;</span> |     #F5DEB3     |   (245,222,179)   |          wheat          | 小麦          |
| <span style="background-color:#FFF8DC">&emsp;&emsp;</span> |     #FFF8DC     |   (255,248,220)   |        corn silk        | 玉米须        |
| <span style="background-color:#FFFACD">&emsp;&emsp;</span> |     #FFFACD     |   (255,250,205)   |      lemon chiffon      | 柠檬雪纺      |
| <span style="background-color:#FAFAD2">&emsp;&emsp;</span> |     #FAFAD2     |   (250,250,210)   | light golden rod yellow | 淡金黄色      |
| <span style="background-color:#FFFFE0">&emsp;&emsp;</span> |     #FFFFE0     |   (255,255,224)   |      light yellow       | 淡黄色        |
| <span style="background-color:#8B4513">&emsp;&emsp;</span> |     #8B4513     |    (139,69,19)    |      saddle brown       | 马鞍棕色      |
| <span style="background-color:#A0522D">&emsp;&emsp;</span> |     #A0522D     |    (160,82,45)    |         sienna          | 赭色          |
| <span style="background-color:#D2691E">&emsp;&emsp;</span> |     #D2691E     |   (210,105,30)    |        chocolate        | 巧克力        |
| <span style="background-color:#CD853F">&emsp;&emsp;</span> |     #CD853F     |   (205,133,63)    |          peru           | 秘鲁          |
| <span style="background-color:#F4A460">&emsp;&emsp;</span> |     #F4A460     |   (244,164,96)    |       sandy brown       | 沙棕色        |
| <span style="background-color:#DEB887">&emsp;&emsp;</span> |     #DEB887     |   (222,184,135)   |       burly wood        | 魁梧木头      |
| <span style="background-color:#D2B48C">&emsp;&emsp;</span> |     #D2B48C     |   (210,180,140)   |           tan           | 棕褐色        |
| <span style="background-color:#BC8F8F">&emsp;&emsp;</span> |     #BC8F8F     |   (188,143,143)   |       rosy brown        | 玫瑰棕色      |
| <span style="background-color:#FFE4B5">&emsp;&emsp;</span> |     #FFE4B5     |   (255,228,181)   |        moccasin         | 软皮鞋        |
| <span style="background-color:#FFDEAD">&emsp;&emsp;</span> |     #FFDEAD     |   (255,222,173)   |      navajo white       | 纳瓦霍白      |
| <span style="background-color:#FFDAB9">&emsp;&emsp;</span> |     #FFDAB9     |   (255,218,185)   |       peach puff        | 桃子泡芙      |
| <span style="background-color:#FFE4E1">&emsp;&emsp;</span> |     #FFE4E1     |   (255,228,225)   |       misty rose        | 迷雾玫瑰      |
| <span style="background-color:#FFF0F5">&emsp;&emsp;</span> |     #FFF0F5     |   (255,240,245)   |     lavender blush      | 薰衣草腮红    |
| <span style="background-color:#FAF0E6">&emsp;&emsp;</span> |     #FAF0E6     |   (250,240,230)   |          linen          | 亚麻布        |
| <span style="background-color:#FDF5E6">&emsp;&emsp;</span> |     #FDF5E6     |   (253,245,230)   |        old lace         | 旧花边        |
| <span style="background-color:#FFEFD5">&emsp;&emsp;</span> |     #FFEFD5     |   (255,239,213)   |       papaya whip       | 木瓜鞭        |
| <span style="background-color:#FFF5EE">&emsp;&emsp;</span> |     #FFF5EE     |   (255,245,238)   |        sea shell        | 海贝壳        |
| <span style="background-color:#F5FFFA">&emsp;&emsp;</span> |     #F5FFFA     |   (245,255,250)   |       mint cream        | 薄荷奶油      |
| <span style="background-color:#708090">&emsp;&emsp;</span> |     #708090     |   (112,128,144)   |       slate gray        | 板岩灰色      |
| <span style="background-color:#778899">&emsp;&emsp;</span> |     #778899     |   (119,136,153)   |    light slate gray     | 浅石灰色      |
| <span style="background-color:#B0C4DE">&emsp;&emsp;</span> |     #B0C4DE     |   (176,196,222)   |    light steel blue     | 轻钢蓝        |
| <span style="background-color:#E6E6FA">&emsp;&emsp;</span> |     #E6E6FA     |   (230,230,250)   |        lavender         | 薰衣草        |
| <span style="background-color:#FFFAF0">&emsp;&emsp;</span> |     #FFFAF0     |   (255,250,240)   |      floral white       | 花白          |
| <span style="background-color:#F0F8FF">&emsp;&emsp;</span> |     #F0F8FF     |   (240,248,255)   |       alice blue        | 爱丽丝蓝      |
| <span style="background-color:#F8F8FF">&emsp;&emsp;</span> |     #F8F8FF     |   (248,248,255)   |       ghost white       | 鬼白          |
| <span style="background-color:#F0FFF0">&emsp;&emsp;</span> |     #F0FFF0     |   (240,255,240)   |        honeydew         | 甘露          |
| <span style="background-color:#FFFFF0">&emsp;&emsp;</span> |     #FFFFF0     |   (255,255,240)   |          ivory          | 象牙          |
| <span style="background-color:#F0FFFF">&emsp;&emsp;</span> |     #F0FFFF     |   (240,255,255)   |          azure          | 天蓝色        |
| <span style="background-color:#FFFAFA">&emsp;&emsp;</span> |     #FFFAFA     |   (255,250,250)   |          snow           | 雪            |
| <span style="background-color:#696969">&emsp;&emsp;</span> |     #696969     |   (105,105,105)   |    dim gray/dim grey    | 暗灰色/暗灰色 |
| <span style="background-color:#A9A9A9">&emsp;&emsp;</span> |     #A9A9A9     |   (169,169,169)   |   dark gray/dark grey   | 深灰/深灰     |
| <span style="background-color:#D3D3D3">&emsp;&emsp;</span> |     #D3D3D3     |   (211,211,211)   |  light gray/light grey  | 浅灰/浅灰     |
| <span style="background-color:#DCDCDC">&emsp;&emsp;</span> |     #DCDCDC     |   (220,220,220)   |        gainsboro        | 格斯伯勒      |
| <span style="background-color:#F5F5F5">&emsp;&emsp;</span> |     #F5F5F5     |   (245,245,245)   |       white smoke       | 白色烟        |
