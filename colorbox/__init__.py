__version__ = "0.1.1"
__author__ = "zhangxianbing"

import random
from itertools import cycle
from typing import Optional, Tuple

# 推荐安装 vscode 插件 Color Highlight 更直观地查看以下颜色
# 来源： <https://www.rapidtables.com/web/color/RGB_Color.html>
# | zh_name       |         en_name         | Hex Code#RRGGBB | Decimal CodeR,G,B |
_color_map_text = """
|     #FF0000     |     (255,0,0)     |           red           | 红色          |
|     #FFA500     |    (255,165,0)    |         orange          | 橙色          |
|     #FFFF00     |    (255,255,0)    |         yellow          | 黄色          |
|     #008000     |     (0,128,0)     |          green          | 绿色          |
|     #00FFFF     |    (0,255,255)    |        cyan/aqua        | 青色/水色     |
|     #0000FF     |     (0,0,255)     |          blue           | 蓝色          |
|     #FF00FF     |    (255,0,255)    |     magenta/fuchsia     | 洋红色/紫红色 |
|     #7FFFD4     |   (127,255,212)   |       aqua marine       | 海洋蓝        |
|     #FF2400     |    (255,36,0)     |         scarlet         | 猩红色        |
|     #00FF00     |     (0,255,0)     |          lime           | 酸橙绿        |
|     #FFFFFF     |   (255,255,255)   |          white          | 白色          |
|     #C0C0C0     |   (192,192,192)   |         silver          | 银色          |
|     #808080     |   (128,128,128)   |          gray           | 灰色          |
|     #008080     |    (0,128,128)    |          teal           | 青色          |
|     #800000     |     (128,0,0)     |         maroon          | 栗色          |
|     #808000     |    (128,128,0)    |          olive          | 橄榄色        |
|     #800080     |    (128,0,128)    |         purple          | 紫色          |
|     #000080     |     (0,0,128)     |          navy           | 海军色        |
|     #FFD700     |    (255,215,0)    |          gold           | 金色          |
|     #B8860B     |   (184,134,11)    |     dark golden rod     | 暗金棒        |
|     #DAA520     |   (218,165,32)    |       golden rod        | 金棒          |
|     #000000     |      (0,0,0)      |          black          | 黑色          |
|     #EEE8AA     |   (238,232,170)   |     pale golden rod     | 淡金色棒      |
|     #BDB76B     |   (189,183,107)   |       dark khaki        | 深卡其色      |
|     #F0E68C     |   (240,230,140)   |          khaki          | 卡其色        |
|     #9ACD32     |   (154,205,50)    |      yellow green       | 黄绿色        |
|     #556B2F     |    (85,107,47)    |    dark olive green     | 深橄榄绿      |
|     #6B8E23     |   (107,142,35)    |       olive drab        | 橄榄色        |
|     #7FFF00     |    (127,255,0)    |       chart reuse       | 黄绿色        |
|     #ADFF2F     |   (173,255,47)    |      green yellow       | 黄绿色        |
|     #006400     |     (0,100,0)     |       dark green        | 深绿色        |
|     #228B22     |    (34,139,34)    |      forest green       | 森林绿        |
|     #32CD32     |    (50,205,50)    |       lime green        | 柠檬绿        |
|     #90EE90     |   (144,238,144)   |       light green       | 浅绿色        |
|     #8FBC8F     |   (143,188,143)   |     dark sea green      | 深海绿色      |
|     #00FA9A     |    (0,250,154)    |   medium spring green   | 中春绿        |
|     #00FF7F     |    (0,255,127)    |      spring green       | 春绿          |
|     #2E8B57     |    (46,139,87)    |        sea green        | 海绿色        |
|     #66CDAA     |   (102,205,170)   |   medium aqua marine    | 中型海蓝      |
|     #3CB371     |   (60,179,113)    |    medium sea green     | 中海绿        |
|     #20B2AA     |   (32,178,170)    |     light sea green     | 浅海绿色      |
|     #2F4F4F     |    (47,79,79)     |     dark slate gray     | 深石板灰      |
|     #008B8B     |    (0,139,139)    |        dark cyan        | 深青色        |
|     #E0FFFF     |   (224,255,255)   |       light cyan        | 淡青色        |
|     #00CED1     |    (0,206,209)    |     dark turquoise      | 深绿松石      |
|     #40E0D0     |   (64,224,208)    |        turquoise        | 绿松石        |
|     #48D1CC     |   (72,209,204)    |    medium turquoise     | 中绿松石      |
|     #AFEEEE     |   (175,238,238)   |     pale turquoise      | 淡绿松石      |
|     #B0E0E6     |   (176,224,230)   |       powder blue       | 粉蓝色        |
|     #5F9EA0     |   (95,158,160)    |       cadet blue        | 学员蓝        |
|     #4682B4     |   (70,130,180)    |       steel blue        | 钢蓝色        |
|     #6495ED     |   (100,149,237)   |    corn flower blue     | 玉米花蓝色    |
|     #00BFFF     |    (0,191,255)    |      deep sky blue      | 深蓝色        |
|     #1E90FF     |   (30,144,255)    |       dodger blue       | 道奇蓝        |
|     #ADD8E6     |   (173,216,230)   |       light blue        | 浅蓝          |
|     #87CEEB     |   (135,206,235)   |        sky blue         | 天蓝色        |
|     #87CEFA     |   (135,206,250)   |     light sky blue      | 淡天蓝色      |
|     #191970     |    (25,25,112)    |      midnight blue      | 午夜蓝        |
|     #00008B     |     (0,0,139)     |        dark blue        | 深蓝          |
|     #0000CD     |     (0,0,205)     |       medium blue       | 中蓝色        |
|     #4169E1     |   (65,105,225)    |       royal blue        | 宝蓝色        |
|     #8A2BE2     |   (138,43,226)    |       blue violet       | 紫罗兰色      |
|     #4B0082     |    (75,0,130)     |         indigo          | 靛青          |
|     #483D8B     |    (72,61,139)    |     dark slate blue     | 深石板蓝      |
|     #6A5ACD     |   (106,90,205)    |       slate blue        | 石板蓝        |
|     #7B68EE     |   (123,104,238)   |    medium slate blue    | 中石板蓝      |
|     #9370DB     |   (147,112,219)   |      medium purple      | 中紫色        |
|     #8B008B     |    (139,0,139)    |      dark magenta       | 深洋红色      |
|     #9400D3     |    (148,0,211)    |       dark violet       | 深紫色        |
|     #9932CC     |   (153,50,204)    |       dark orchid       | 暗兰花        |
|     #BA55D3     |   (186,85,211)    |      medium orchid      | 中等兰花      |
|     #D8BFD8     |   (216,191,216)   |         thistle         | 蓟            |
|     #DDA0DD     |   (221,160,221)   |          plum           | 李子          |
|     #EE82EE     |   (238,130,238)   |         violet          | 紫色          |
|     #DA70D6     |   (218,112,214)   |         orchid          | 兰花          |
|     #C71585     |   (199,21,133)    |    medium violet red    | 中紫红色      |
|     #DB7093     |   (219,112,147)   |     pale violet red     | 淡紫红色      |
|     #FF1493     |   (255,20,147)    |        deep pink        | 深粉色        |
|     #FF69B4     |   (255,105,180)   |        hot pink         | 亮粉色        |
|     #FFB6C1     |   (255,182,193)   |       light pink        | 浅粉色        |
|     #FFC0CB     |   (255,192,203)   |          pink           | 粉色          |
|     #FAEBD7     |   (250,235,215)   |      antique white      | 古色古香白色  |
|     #F5F5DC     |   (245,245,220)   |          beige          | 浅褐色        |
|     #FFE4C4     |   (255,228,196)   |         bisque          | 浓汤          |
|     #FFEBCD     |   (255,235,205)   |     blanched almond     | 漂白杏仁      |
|     #F5DEB3     |   (245,222,179)   |          wheat          | 小麦          |
|     #FFF8DC     |   (255,248,220)   |        corn silk        | 玉米须        |
|     #FFFACD     |   (255,250,205)   |      lemon chiffon      | 柠檬雪纺      |
|     #FAFAD2     |   (250,250,210)   | light golden rod yellow | 淡金黄色      |
|     #FFFFE0     |   (255,255,224)   |      light yellow       | 淡黄色        |
|     #8B4513     |    (139,69,19)    |      saddle brown       | 马鞍棕色      |
|     #A0522D     |    (160,82,45)    |         sienna          | 赭色          |
|     #D2691E     |   (210,105,30)    |        chocolate        | 巧克力        |
|     #CD853F     |   (205,133,63)    |          peru           | 秘鲁          |
|     #F4A460     |   (244,164,96)    |       sandy brown       | 沙棕色        |
|     #DEB887     |   (222,184,135)   |       burly wood        | 魁梧木头      |
|     #D2B48C     |   (210,180,140)   |           tan           | 棕褐色        |
|     #BC8F8F     |   (188,143,143)   |       rosy brown        | 玫瑰棕色      |
|     #FFE4B5     |   (255,228,181)   |        moccasin         | 软皮鞋        |
|     #FFDEAD     |   (255,222,173)   |      navajo white       | 纳瓦霍白      |
|     #FFDAB9     |   (255,218,185)   |       peach puff        | 桃子泡芙      |
|     #FFE4E1     |   (255,228,225)   |       misty rose        | 迷雾玫瑰      |
|     #FFF0F5     |   (255,240,245)   |     lavender blush      | 薰衣草腮红    |
|     #FAF0E6     |   (250,240,230)   |          linen          | 亚麻布        |
|     #FDF5E6     |   (253,245,230)   |        old lace         | 旧花边        |
|     #FFEFD5     |   (255,239,213)   |       papaya whip       | 木瓜鞭        |
|     #FFF5EE     |   (255,245,238)   |        sea shell        | 海贝壳        |
|     #F5FFFA     |   (245,255,250)   |       mint cream        | 薄荷奶油      |
|     #708090     |   (112,128,144)   |       slate gray        | 板岩灰色      |
|     #778899     |   (119,136,153)   |    light slate gray     | 浅石灰色      |
|     #B0C4DE     |   (176,196,222)   |    light steel blue     | 轻钢蓝        |
|     #E6E6FA     |   (230,230,250)   |        lavender         | 薰衣草        |
|     #FFFAF0     |   (255,250,240)   |      floral white       | 花白          |
|     #F0F8FF     |   (240,248,255)   |       alice blue        | 爱丽丝蓝      |
|     #F8F8FF     |   (248,248,255)   |       ghost white       | 鬼白          |
|     #F0FFF0     |   (240,255,240)   |        honeydew         | 甘露          |
|     #FFFFF0     |   (255,255,240)   |          ivory          | 象牙          |
|     #F0FFFF     |   (240,255,255)   |          azure          | 天蓝色        |
|     #FFFAFA     |   (255,250,250)   |          snow           | 雪            |
|     #696969     |   (105,105,105)   |    dim gray/dim grey    | 暗灰色/暗灰色 |
|     #A9A9A9     |   (169,169,169)   |   dark gray/dark grey   | 深灰/深灰     |
|     #D3D3D3     |   (211,211,211)   |  light gray/light grey  | 浅灰/浅灰     |
|     #DCDCDC     |   (220,220,220)   |        gainsboro        | 格斯伯勒      |
|     #F5F5F5     |   (245,245,245)   |       white smoke       | 白色烟        |
"""

_color_map = None


def _get_color_map():
    global _color_map
    if _color_map:
        return _color_map

    _color_map = {"rgb": {}, "bgr": {}, "hex": {}}

    for line in _color_map_text.strip().split("\n"):
        _, hex_txt, rgb_txt, en_names, zh_names, _ = line.split("|")
        rgb = tuple(map(int, rgb_txt.strip()[1:-1].split(",")))
        bgr = tuple(reversed(rgb))
        hex = hex_txt.strip()

        for name in zh_names.strip().split("/"):
            _color_map["rgb"][name] = rgb
            _color_map["bgr"][name] = bgr
            _color_map["hex"][name] = hex

        for name in en_names.strip().split("/"):
            _color_map["rgb"][name] = rgb
            _color_map["bgr"][name] = bgr
            _color_map["hex"][name] = hex

    _color_map["rgb_list"] = list(_color_map["rgb"].values())
    _color_map["bgr_list"] = list(_color_map["bgr"].values())
    _color_map["hex_list"] = list(_color_map["hex"].values())

    return _color_map


def rgb(name: str) -> Optional[Tuple[int, int, int]]:
    """Return rgb tuple if given `name` is in color map, `None` otherwise.

    Args:
        name (str): color name

    Returns:
        Optional[Tuple[int, int, int]]: rgb tuple
    """
    cm = _get_color_map()
    return cm["rgb"].get(name)


def rand_rgb(i: int = None) -> Tuple[int, int, int]:
    """Return random rgb tuple of color in color map.

    Args:
        i (int, optional): color index in color list if given. Defaults to None.

    Returns:
        Tuple[int, int, int]: rgb tuple
    """
    cm = _get_color_map()
    cl = cm["rgb_list"]
    if i is None:
        return random.choice(cl)

    return cl[i % (len(cl))]


def cycle_rgb():
    """Return cycle iterator for rbg color.

    Returns:
        [type]: [description]
    """
    cm = _get_color_map()
    cl = cm["rgb_list"]
    return cycle(cl)


# 注: opencv 里颜色通道顺序为BGR
def bgr(name: str) -> Optional[Tuple[int, int, int]]:
    """Return bgr tuple if given `name` is in color map, `None` otherwise.

    Args:
        name (str): color name

    Returns:
        Optional[Tuple[int, int, int]]: bgr tuple
    """
    cm = _get_color_map()
    return cm["bgr"].get(name)


def rand_bgr(i: int = None) -> Tuple[int, int, int]:
    """Return random bgr tuple of color in color map.

    Args:
        i (int, optional): color index in color list if given. Defaults to None.

    Returns:
        Tuple[int, int, int]: bgr tuple
    """
    cm = _get_color_map()
    cl = cm["bgr_list"]
    if i is None:
        return random.choice(cl)

    return cl[i % (len(cl))]


def cycle_bgr():
    """Return cycle iterator for bgr color.

    Returns:
        [type]: [description]
    """
    cm = _get_color_map()
    cl = cm["bgr_list"]
    return cycle(cl)


def hex(name: str) -> Optional[str]:
    """Return hex string if given `name` is in color map, `None` otherwise.

    Args:
        name (str): color name

    Returns:
        Optional[str]: hex string
    """
    cm = _get_color_map()
    return cm["hex"].get(name)


def rand_hex(i: int = None) -> str:
    """Return hex string of color in color map.

    Args:
        i (int, optional): color index in color list if given. Defaults to None.

    Returns:
        str: color hex code
    """
    cm = _get_color_map()
    cl = cm["hex_list"]
    if i is None:
        return random.choice(cl)

    return cl[i % (len(cl))]


def cycle_hex():
    """Return cycle iterator for color hex code.

    Returns:
        [type]: [description]
    """
    cm = _get_color_map()
    cl = cm["hex_list"]
    return cycle(cl)


def random_color() -> Tuple[int, int, int]:
    """Return random color tuple"""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


if __name__ == "__main__":
    from pprint import pprint

    pprint(_get_color_map())

    # for i in cycle_rgb():
    #     print(i)
