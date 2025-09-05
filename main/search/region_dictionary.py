# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AMapExtension
                                 Region Dictionary.
 This file defines city names and the provinces they belong to.
                              -------------------
        begin                : 2025-09-05
        copyright            : (C) 2025 by phoenix-gis
        email                : phoenixgis@sina.com
        website              : phoenix-gis.cn
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import json

class RegionDictionary:

    @staticmethod
    def get_json():
        return json.loads("""
        [
    {
        "provice": "北京市"
    },
    {
        "provice": "天津市"
    },
    {
        "provice": "上海市"
    },
    {
        "provice": "重庆市"
    },
    {
        "provice": "安徽省",
        "city": [
            {
                "name": "合肥"
            },
            {
                "name": "芜湖"
            },
            {
                "name": "蚌埠"
            },
            {
                "name": "淮南"
            },
            {
                "name": "马鞍山"
            },
            {
                "name": "淮北"
            },
            {
                "name": "铜陵"
            },
            {
                "name": "安庆"
            },
            {
                "name": "黄山"
            },
            {
                "name": "滁州"
            },
            {
                "name": "阜阳"
            },
            {
                "name": "宿州"
            },
            {
                "name": "六安"
            },
            {
                "name": "亳州"
            },
            {
                "name": "池州"
            },
            {
                "name": "宣城"
            }
        ]
    },
    {
        "provice": "福建省",
        "city": [
            {
                "name": "福州"
            },
            {
                "name": "厦门"
            },
            {
                "name": "莆田"
            },
            {
                "name": "三明"
            },
            {
                "name": "泉州"
            },
            {
                "name": "漳州"
            },
            {
                "name": "南平"
            },
            {
                "name": "龙岩"
            },
            {
                "name": "宁德"
            }
        ]
    },
    {
        "provice": "广东省",
        "city": [
            {
                "name": "广州"
            },
            {
                "name": "韶关"
            },
            {
                "name": "深圳"
            },
            {
                "name": "珠海"
            },
            {
                "name": "汕头"
            },
            {
                "name": "佛山"
            },
            {
                "name": "江门"
            },
            {
                "name": "湛江"
            },
            {
                "name": "茂名"
            },
            {
                "name": "肇庆"
            },
            {
                "name": "惠州"
            },
            {
                "name": "梅州"
            },
            {
                "name": "汕尾"
            },
            {
                "name": "河源"
            },
            {
                "name": "阳江"
            },
            {
                "name": "清远"
            },
            {
                "name": "东莞"
            },
            {
                "name": "中山"
            },
            {
                "name": "潮州"
            },
            {
                "name": "揭阳"
            },
            {
                "name": "云浮"
            }
        ]
    },
    {
        "provice": "广西壮族自治区",
        "city": [
            {
                "name": "南宁"
            },
            {
                "name": "柳州"
            },
            {
                "name": "桂林"
            },
            {
                "name": "梧州"
            },
            {
                "name": "北海"
            },
            {
                "name": "防城港"
            },
            {
                "name": "钦州"
            },
            {
                "name": "贵港"
            },
            {
                "name": "玉林"
            },
            {
                "name": "百色"
            },
            {
                "name": "贺州"
            },
            {
                "name": "河池"
            },
            {
                "name": "来宾"
            },
            {
                "name": "崇左"
            }
        ]
    },
    {
        "provice": "贵州省",
        "city": [
            {
                "name": "贵阳"
            },
            {
                "name": "六盘水"
            },
            {
                "name": "遵义"
            },
            {
                "name": "安顺"
            },
            {
                "name": "毕节"
            },
            {
                "name": "铜仁"
            },
            {
                "name": "黔西南布依族苗族自治州"
            },
            {
                "name": "黔东南苗族侗族自治州"
            },
            {
                "name": "黔南布依族苗族自治州"
            }
        ]
    },
    {
        "provice": "甘肃省",
        "city": [
            {
                "name": "兰州"
            },
            {
                "name": "嘉峪关"
            },
            {
                "name": "金昌"
            },
            {
                "name": "白银"
            },
            {
                "name": "天水"
            },
            {
                "name": "武威"
            },
            {
                "name": "张掖"
            },
            {
                "name": "平凉"
            },
            {
                "name": "酒泉"
            },
            {
                "name": "庆阳"
            },
            {
                "name": "定西"
            },
            {
                "name": "陇南"
            },
            {
                "name": "临夏回族自治州"
            },
            {
                "name": "甘南藏族自治州"
            }
        ]
    },
    {
        "provice": "河北省",
        "city": [
            {
                "name": "石家庄"
            },
            {
                "name": "唐山"
            },
            {
                "name": "秦皇岛"
            },
            {
                "name": "邯郸"
            },
            {
                "name": "邢台"
            },
            {
                "name": "保定"
            },
            {
                "name": "张家口"
            },
            {
                "name": "承德"
            },
            {
                "name": "沧州"
            },
            {
                "name": "廊坊"
            },
            {
                "name": "衡水"
            }
        ]
    },
    {
        "provice": "黑龙江省",
        "city": [
            {
                "name": "哈尔滨"
            },
            {
                "name": "齐齐哈尔"
            },
            {
                "name": "鸡西"
            },
            {
                "name": "鹤岗"
            },
            {
                "name": "双鸭山"
            },
            {
                "name": "大庆"
            },
            {
                "name": "伊春"
            },
            {
                "name": "佳木斯"
            },
            {
                "name": "七台河"
            },
            {
                "name": "牡丹江"
            },
            {
                "name": "黑河"
            },
            {
                "name": "绥化"
            },
            {
                "name": "大兴安岭"
            }
        ]
    },
    {
        "provice": "河南省",
        "city": [
            {
                "name": "郑州"
            },
            {
                "name": "开封"
            },
            {
                "name": "洛阳"
            },
            {
                "name": "平顶山"
            },
            {
                "name": "安阳"
            },
            {
                "name": "鹤壁"
            },
            {
                "name": "新乡"
            },
            {
                "name": "焦作"
            },
            {
                "name": "濮阳"
            },
            {
                "name": "许昌"
            },
            {
                "name": "漯河"
            },
            {
                "name": "三门峡"
            },
            {
                "name": "南阳"
            },
            {
                "name": "商丘"
            },
            {
                "name": "信阳"
            },
            {
                "name": "周口"
            },
            {
                "name": "驻马店"
            },
            {
                "name": "济源"
            }
        ]
    },
    {
        "provice": "湖北省",
        "city": [
            {
                "name": "武汉"
            },
            {
                "name": "黄石"
            },
            {
                "name": "十堰"
            },
            {
                "name": "宜昌"
            },
            {
                "name": "襄阳"
            },
            {
                "name": "鄂州"
            },
            {
                "name": "荆门"
            },
            {
                "name": "孝感"
            },
            {
                "name": "荆州"
            },
            {
                "name": "黄冈"
            },
            {
                "name": "咸宁"
            },
            {
                "name": "随州"
            },
            {
                "name": "恩施土家族苗族自治州"
            },
            {
                "name": "仙桃"
            },
            {
                "name": "潜江"
            },
            {
                "name": "天门"
            },
            {
                "name": "神农架林区"
            }
        ]
    },
    {
        "provice": "湖南省",
        "city": [
            {
                "name": "长沙"
            },
            {
                "name": "株洲"
            },
            {
                "name": "湘潭"
            },
            {
                "name": "衡阳"
            },
            {
                "name": "邵阳"
            },
            {
                "name": "岳阳"
            },
            {
                "name": "常德"
            },
            {
                "name": "张家界"
            },
            {
                "name": "益阳"
            },
            {
                "name": "郴州"
            },
            {
                "name": "永州"
            },
            {
                "name": "怀化"
            },
            {
                "name": "娄底"
            },
            {
                "name": "湘西土家族苗族自治州"
            }
        ]
    },
    {
        "provice": "海南省",
        "city": [
            {
                "name": "海口"
            },
            {
                "name": "三亚"
            },
            {
                "name": "三沙"
            },
            {
                "name": "儋州"
            }
        ]
    },
    {
        "provice": "吉林省",
        "city": [
            {
                "name": "长春"
            },
            {
                "name": "吉林"
            },
            {
                "name": "四平"
            },
            {
                "name": "辽源"
            },
            {
                "name": "通化"
            },
            {
                "name": "白山"
            },
            {
                "name": "松原"
            },
            {
                "name": "白城"
            },
            {
                "name": "延边朝鲜族自治州"
            }
        ]
    },
    {
        "provice": "江苏省",
        "city": [
            {
                "name": "南京"
            },
            {
                "name": "无锡"
            },
            {
                "name": "徐州"
            },
            {
                "name": "常州"
            },
            {
                "name": "苏州"
            },
            {
                "name": "南通"
            },
            {
                "name": "连云港"
            },
            {
                "name": "淮安"
            },
            {
                "name": "盐城"
            },
            {
                "name": "扬州"
            },
            {
                "name": "镇江"
            },
            {
                "name": "泰州"
            },
            {
                "name": "宿迁"
            }
        ]
    },
    {
        "provice": "江西省",
        "city": [
            {
                "name": "南昌"
            },
            {
                "name": "景德镇"
            },
            {
                "name": "萍乡"
            },
            {
                "name": "九江"
            },
            {
                "name": "新余"
            },
            {
                "name": "鹰潭"
            },
            {
                "name": "赣州"
            },
            {
                "name": "吉安"
            },
            {
                "name": "宜春"
            },
            {
                "name": "抚州"
            },
            {
                "name": "上饶"
            }
        ]
    },
    {
        "provice": "辽宁省",
        "city": [
            {
                "name": "沈阳"
            },
            {
                "name": "大连"
            },
            {
                "name": "鞍山"
            },
            {
                "name": "抚顺"
            },
            {
                "name": "本溪"
            },
            {
                "name": "丹东"
            },
            {
                "name": "锦州"
            },
            {
                "name": "营口"
            },
            {
                "name": "阜新"
            },
            {
                "name": "辽阳"
            },
            {
                "name": "盘锦"
            },
            {
                "name": "铁岭"
            },
            {
                "name": "朝阳"
            },
            {
                "name": "葫芦岛"
            }
        ]
    },
    {
        "provice": "内蒙古自治区",
        "city": [
            {
                "name": "呼和浩特"
            },
            {
                "name": "包头"
            },
            {
                "name": "乌海"
            },
            {
                "name": "赤峰"
            },
            {
                "name": "通辽"
            },
            {
                "name": "鄂尔多斯"
            },
            {
                "name": "呼伦贝尔"
            },
            {
                "name": "巴彦淖尔"
            },
            {
                "name": "乌兰察布"
            },
            {
                "name": "兴安盟"
            },
            {
                "name": "锡林郭勒盟"
            },
            {
                "name": "阿拉善盟"
            }
        ]
    },
    {
        "provice": "宁夏回族自治区",
        "city": [
            {
                "name": "银川"
            },
            {
                "name": "石嘴山"
            },
            {
                "name": "吴忠"
            },
            {
                "name": "固原"
            },
            {
                "name": "中卫"
            }
        ]
    },
    {
        "provice": "青海省",
        "city": [
            {
                "name": "西宁"
            },
            {
                "name": "海东"
            },
            {
                "name": "海北藏族自治州"
            },
            {
                "name": "黄南藏族自治州"
            },
            {
                "name": "海南藏族自治州"
            },
            {
                "name": "果洛藏族自治州"
            },
            {
                "name": "玉树藏族自治州"
            },
            {
                "name": "海西蒙古族藏族自治州"
            }
        ]
    },
    {
        "provice": "山西省",
        "city": [
            {
                "name": "太原"
            },
            {
                "name": "大同"
            },
            {
                "name": "阳泉"
            },
            {
                "name": "长治"
            },
            {
                "name": "晋城"
            },
            {
                "name": "朔州"
            },
            {
                "name": "晋中"
            },
            {
                "name": "运城"
            },
            {
                "name": "忻州"
            },
            {
                "name": "临汾"
            },
            {
                "name": "吕梁"
            }
        ]
    },
    {
        "provice": "山东省",
        "city": [
            {
                "name": "济南"
            },
            {
                "name": "青岛"
            },
            {
                "name": "淄博"
            },
            {
                "name": "枣庄"
            },
            {
                "name": "东营"
            },
            {
                "name": "烟台"
            },
            {
                "name": "潍坊"
            },
            {
                "name": "济宁"
            },
            {
                "name": "泰安"
            },
            {
                "name": "威海"
            },
            {
                "name": "日照"
            },
            {
                "name": "莱芜"
            },
            {
                "name": "临沂"
            },
            {
                "name": "德州"
            },
            {
                "name": "聊城"
            },
            {
                "name": "滨州"
            },
            {
                "name": "菏泽"
            }
        ]
    },
    {
        "provice": "四川省",
        "city": [
            {
                "name": "成都"
            },
            {
                "name": "自贡"
            },
            {
                "name": "攀枝花"
            },
            {
                "name": "泸州"
            },
            {
                "name": "德阳"
            },
            {
                "name": "绵阳"
            },
            {
                "name": "广元"
            },
            {
                "name": "遂宁"
            },
            {
                "name": "内江"
            },
            {
                "name": "乐山"
            },
            {
                "name": "南充"
            },
            {
                "name": "眉山"
            },
            {
                "name": "宜宾"
            },
            {
                "name": "广安"
            },
            {
                "name": "达州"
            },
            {
                "name": "雅安"
            },
            {
                "name": "巴中"
            },
            {
                "name": "资阳"
            },
            {
                "name": "阿坝藏族羌族自治州"
            },
            {
                "name": "甘孜藏族自治州"
            },
            {
                "name": "凉山彝族自治州"
            }
        ]
    },
    {
        "provice": "陕西省",
        "city": [
            {
                "name": "西安"
            },
            {
                "name": "铜川"
            },
            {
                "name": "宝鸡"
            },
            {
                "name": "咸阳"
            },
            {
                "name": "渭南"
            },
            {
                "name": "延安"
            },
            {
                "name": "汉中"
            },
            {
                "name": "榆林"
            },
            {
                "name": "安康"
            },
            {
                "name": "商洛"
            }
        ]
    },
    {
        "provice": "台湾省",
        "city": [
            {
                "name": "台北"
            },
            {
                "name": "高雄"
            },
            {
                "name": "台中"
            },
            {
                "name": "台南"
            },
            {
                "name": "新北"
            },
            {
                "name": "基隆"
            },
            {
                "name": "新竹"
            },
            {
                "name": "嘉义"
            }
        ]
    },
    {
        "provice": "西藏自治区",
        "city": [
            {
                "name": "拉萨"
            },
            {
                "name": "日喀则"
            },
            {
                "name": "昌都"
            },
            {
                "name": "林芝"
            },
            {
                "name": "山南"
            },
            {
                "name": "那曲"
            },
            {
                "name": "阿里"
            }
        ]
    },
    {
        "provice": "新疆维吾尔自治区",
        "city": [
            {
                "name": "乌鲁木齐"
            },
            {
                "name": "克拉玛依"
            },
            {
                "name": "吐鲁番"
            },
            {
                "name": "哈密"
            },
            {
                "name": "昌吉回族自治州"
            },
            {
                "name": "博尔塔拉蒙古自治州"
            },
            {
                "name": "巴音郭楞蒙古自治州"
            },
            {
                "name": "阿克苏"
            },
            {
                "name": "克孜勒苏柯尔克孜自治州"
            },
            {
                "name": "喀什"
            },
            {
                "name": "和田"
            },
            {
                "name": "伊犁哈萨克自治州"
            },
            {
                "name": "塔城"
            },
            {
                "name": "阿勒泰"
            },
            {
                "name": "石河子"
            },
            {
                "name": "阿拉尔"
            },
            {
                "name": "图木舒克"
            },
            {
                "name": "五家渠"
            }
        ]
    },
    {
        "provice": "云南省",
        "city": [
            {
                "name": "昆明"
            },
            {
                "name": "曲靖"
            },
            {
                "name": "玉溪"
            },
            {
                "name": "保山"
            },
            {
                "name": "昭通"
            },
            {
                "name": "丽江"
            },
            {
                "name": "普洱"
            },
            {
                "name": "临沧"
            },
            {
                "name": "楚雄彝族自治州"
            },
            {
                "name": "红河哈尼族彝族自治州"
            },
            {
                "name": "文山壮族苗族自治州"
            },
            {
                "name": "西双版纳傣族自治州"
            },
            {
                "name": "大理白族自治州"
            },
            {
                "name": "德宏傣族景颇族自治州"
            },
            {
                "name": "怒江傈僳族自治州"
            },
            {
                "name": "迪庆藏族自治州"
            }
        ]
    },
    {
        "provice": "浙江省",
        "city": [
            {
                "name": "杭州"
            },
            {
                "name": "宁波"
            },
            {
                "name": "温州"
            },
            {
                "name": "嘉兴"
            },
            {
                "name": "湖州"
            },
            {
                "name": "绍兴"
            },
            {
                "name": "金华"
            },
            {
                "name": "衢州"
            },
            {
                "name": "舟山"
            },
            {
                "name": "台州"
            },
            {
                "name": "丽水"
            }
        ]
    },
    {
        "provice": "香港特别行政区"
    },
    {
        "provice": "澳门特别行政区"
    }
]
""")