
$(window).load(function () {
    $(".loading").fadeOut()
})

/****/
$(document).ready(function () {
    var whei = $(window).width()
    $("html").css({fontSize: whei / 20})
    $(window).resize(function () {
        var whei = $(window).width()
        $("html").css({fontSize: whei / 20})
    });
});


$(window).load(function () {
    $(".loading").fadeOut()
})
$(function () {
    echarts_1()
    echarts_2()
    echarts_3()
    echarts_4()
    // echarts_5()
    echarts_6()

    function echarts_1() {

        $.ajax({
            url: "/api/echarts1",
            type: 'GET',
            async: false,
            success: function (Response) {
                var myChart = echarts.init(document.getElementById('echarts1'));
                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {type: 'shadow'},
                    }, "grid": {
                        "top": "20%",
                        "right": "50",
                        "bottom": "20",
                        "left": "30",
                    },
                    legend: {
                        data: ['播放数', '弹幕数', '分享数', '收藏数', "评论数"],
                        right: 'center', width: '100%',
                        textStyle: {
                            color: "#fff"
                        },
                        itemWidth: 12,
                        itemHeight: 10,
                    },


                    "xAxis": [
                        {
                            "type": "category",
                            data: ['综合热门', '每周必看', '入站必刷', '热播排行'],
                            axisLine: {lineStyle: {color: "rgba(255,255,255,.1)"}},
                            axisLabel: {
                                textStyle: {color: "rgba(255,255,255,.7)", fontSize: '14',},
                            },

                        },
                    ],
                    "yAxis": [
                        {
                            "type": "value",
                            "name": "单位万",
                            axisTick: {show: false},
                            splitLine: {
                                show: false,

                            },
                            "axisLabel": {
                                "show": true,
                                fontSize: 14,
                                color: "rgba(255,255,255,.6)"

                            },
                            axisLine: {
                                min: 0,
                                max: 10,
                                lineStyle: {color: 'rgba(255,255,255,.1)'}
                            },//左线色

                        },
                        {
                            "type": "value",
                            "name": "增速",
                            "show": true,
                            "axisLabel": {
                                "show": true,
                                fontSize: 14,
                                formatter: "{value} %",
                                color: "rgba(255,255,255,.6)"
                            },
                            axisTick: {show: false},
                            axisLine: {lineStyle: {color: 'rgba(255,255,255,.1)'}},//右线色
                            splitLine: {show: true, lineStyle: {color: 'rgba(255,255,255,.1)'}},//x轴线
                        },
                    ],
                    "series": [
                        {
                            "name": "播放数",
                            "type": "bar",
                            "data": Response.bf_total_list,
                            "barWidth": "15%",
                            "itemStyle": {
                                "normal": {
                                    barBorderRadius: 15,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#8bd46e'
                                    }, {
                                        offset: 1,
                                        color: '#09bcb7'
                                    }]),
                                }
                            },
                            "barGap": "0.2"
                        },
                        {
                            "name": "弹幕数",
                            "type": "bar",
                            "data": Response.dm_total_list,
                            "barWidth": "15%",
                            "itemStyle": {
                                "normal": {
                                    barBorderRadius: 15,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#248ff7'
                                    }, {
                                        offset: 1,
                                        color: '#6851f1'
                                    }]),
                                }
                            },
                            "barGap": "0.2"
                        },
                        {
                            "name": "分享数",
                            "type": "bar",
                            "data": Response.fx_total_list,
                            "barWidth": "15%",
                            "itemStyle": {
                                "normal": {
                                    barBorderRadius: 15,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#fccb05'
                                    }, {
                                        offset: 1,
                                        color: '#f5804d'
                                    }]),
                                }
                            },
                            "barGap": "0.2"
                        },
                        {
                            "name": "收藏数",
                            "type": "line",
                            smooth: true,
                            "yAxisIndex": 1,
                            "data": Response.sc_total_list,
                            lineStyle: {
                                normal: {
                                    width: 2
                                },
                            },
                            "itemStyle": {
                                "normal": {
                                    "color": "#86d370",

                                }
                            },

                        },
                        {
                            "name": "评论数",
                            "type": "line",
                            "yAxisIndex": 1,

                            "data": Response.pl_total_list,
                            lineStyle: {
                                normal: {
                                    width: 2
                                },
                            },
                            "itemStyle": {
                                "normal": {
                                    "color": "#3496f8",

                                }
                            },
                            "smooth": true
                        },

                    ]
                };
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();
                });

                // 基于准备好的dom，初始化echarts实例
                var myChart5 = echarts.init(document.getElementById('echarts5'));

                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {type: 'shadow'},
                    }, "grid": {
                        "top": "15%",
                        "right": "10%",
                        "bottom": "20",
                        "left": "10%",
                    },
                    legend: {
                        data: ['字段1', '字段2'],
                        right: 'center',
                        top: 0,
                        textStyle: {
                            color: "#fff"
                        },
                        itemWidth: 12,
                        itemHeight: 10,
                    },
                    "xAxis": [
                        {
                            "type": "category",

                            data: ['综合热门', '每周必看', '入站必刷', '热播排行'],
                            axisLine: {lineStyle: {color: "rgba(255,255,255,.1)"}},
                            axisLabel: {
                                textStyle: {color: "rgba(255,255,255,.7)", fontSize: '14',},
                            },

                        },
                    ],
                    "yAxis": [
                        {
                            "type": "value",
                            "name": "单位1",
                            splitLine: {show: false},
                            axisTick: {show: false},
                            "axisLabel": {
                                "show": true,
                                color: "rgba(255,255,255,.6)"

                            },
                            axisLine: {lineStyle: {color: 'rgba(255,255,255,.1)'}},//左线色

                        },
                        {
                            "type": "value",
                            "name": "单位2",
                            "show": true,
                            axisTick: {show: false},
                            "axisLabel": {
                                "show": true,
                                formatter: "{value} %",
                                color: "rgba(255,255,255,.6)"
                            },
                            axisLine: {lineStyle: {color: 'rgba(255,255,255,.1)'}},//右线色
                            splitLine: {show: true, lineStyle: {color: 'rgba(255,255,255,.1)'}},//x轴线
                        },
                    ],
                    "series": [

                        {
                            "name": "数量",
                            "type": "bar",
                            "data": Response.echarts_5,
                            "barWidth": "20%",

                            "itemStyle": {
                                "normal": {
                                    barBorderRadius: 15,
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: '#fccb05'
                                    }, {
                                        offset: 1,
                                        color: '#f5804d'
                                    }]),
                                }
                            },
                            "barGap": "0"
                        },
                        {
                            "name": "数量",
                            "type": "line",
                            "yAxisIndex": 1,

                            "data": Response.echarts_5,
                            lineStyle: {
                                normal: {
                                    width: 2
                                },
                            },
                            "itemStyle": {
                                "normal": {
                                    "color": "#ff3300",

                                }
                            },
                            "smooth": true
                        }
                    ]
                };
                // 使用刚指定的配置项和数据显示图表。
                myChart5.setOption(option);
                window.addEventListener("resize", function () {
                    myChart5.resize();
                });

            }
        });

    }




    function echarts_2() {

        $.ajax({
            url: "/api/echarts2",
            type: 'GET',
            async: false,
            success: function (Response) {

                // 基于准备好的dom，初始化echarts实例
                var myChart = echarts.init(document.getElementById('echarts2'));

                option = {
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {type: 'shadow'},
                        // formatter:'{c}' ,
                    },
                    grid: {
                        left: '0',
                        top: '30',
                        right: '10',
                        bottom: '-20',
                        containLabel: true
                    },
                    legend: {
                        data: ['视频发布量'],
                        right: 'center',
                        top: 0,
                        textStyle: {
                            color: "#fff"
                        },
                        itemWidth: 12,
                        itemHeight: 10,
                        // itemGap: 35
                    },

                    xAxis: [{
                        type: 'category',
                        boundaryGap: false,
                        axisLabel: {
                            rotate: -90,
                            textStyle: {
                                color: "rgba(255,255,255,.6)",
                                fontSize: 14,

                            },
                        },
                        axisLine: {
                            lineStyle: {
                                color: 'rgba(255,255,255,.1)'
                            }

                        },

                        data: Response.time_list

                    }, {

                        axisPointer: {show: false},
                        axisLine: {show: false},
                        position: 'bottom',
                        offset: 20,


                    }],

                    yAxis: [{
                        type: 'value',
                        axisTick: {show: false},
                        // splitNumber: 6,
                        axisLine: {
                            lineStyle: {
                                color: 'rgba(255,255,255,.1)'
                            }
                        },
                        axisLabel: {
                            formatter: "{value} %",
                            textStyle: {
                                color: "rgba(255,255,255,.6)",
                                fontSize: 14,
                            },
                        },

                        splitLine: {
                            lineStyle: {
                                color: 'rgba(255,255,255,.1)'
                            }
                        }
                    }],
                    series: [
                        {
                            name: '发布视频量',
                            type: 'line',
                            smooth: true,
                            symbol: 'circle',
                            symbolSize: 5,
                            showSymbol: false,
                            lineStyle: {
                                normal: {
                                    color: 'rgb(222,18,217)',
                                    width: 2
                                }
                            },
                            areaStyle: {
                                normal: {
                                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                        offset: 0,
                                        color: 'rgba(228, 228, 126, .2)'
                                    }, {
                                        offset: 1,
                                        color: 'rgba(228, 228, 126, 0)'
                                    }], false),
                                    shadowColor: 'rgba(0, 0, 0, 0.1)',
                                }
                            },
                            itemStyle: {
                                normal: {
                                    color: 'rgba(228, 228, 126, 1)',
                                    borderColor: 'rgba(228, 228, 126, .1)',
                                    borderWidth: 12
                                }
                            },
                            data: Response.xa_list

                        },
                    ]
                };
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();
                });

            }
        });


    }


    function echarts_3() {

        $.ajax({
            url: "/api/echarts3",
            type: 'GET',
            async: false,
            success: function (Response) {
                // 基于准备好的dom，初始化echarts实例
                var myChart = echarts.init(document.getElementById('echarts3'));
                option = {

                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'shadow'
                        }
                    },
                    grid: {
                        top: '30%',
                        right: '3%',
                        left: '4%',
                        bottom: '25%'
                    },
                    dataZoom: [
                        {
                            show: true,
                            realtime: true,
                            start: 0,
                            end: 20
                        },
                        {
                            type: 'inside',
                            realtime: true,
                            start: 0,
                            end: 20
                        }
                    ],
                    xAxis: [{
                        type: 'category',
                        axisLabel: {
                            color: '#fff',
                            interval: 0
                        },
                        axisLine: {
                            show: true,
                            lineStyle: {
                                color: '#0a3e98'
                            }
                        },
                        axisTick: {
                            show: false,
                        },
                        splitLine: {
                            show: false,
                            lineStyle: {
                                color: '#195384',
                                type: "dotted",
                            }
                        },
                        data: Response.x_list,
                    }],
                    yAxis: [
                        {
                            type: 'value',
                            name: "条",
                            min: 0,
                            position: 'left',
                            nameTextStyle: {
                                color: "#fff",
                                fontSize: 16,
                            },
                            axisLine: {
                                lineStyle: {
                                    color: '#0a3e98'
                                }
                            },
                            axisTick: {
                                show: false,
                            },
                            splitLine: {
                                show: true,
                                lineStyle: {
                                    color: '#0a3e98',
                                    type: "dotted",
                                }
                            },
                            axisLabel: {
                                formatter: '{value}',
                                textStyle: {
                                    color: "#fff",
                                }
                            },
                        }
                    ],

                    series: [{
                        name: '标签',
                        type: 'bar',
                        barWidth: 23, //柱子宽度
                        barGap: 0.3, //柱子之间间距
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(0, 0, 0, 0.7, [{
                                    offset: 0,
                                    color: "#d0b415"
                                },
                                    {
                                        offset: 1,
                                        color: "#425052"
                                    }
                                ]),
                            }
                        },
                        label: {
                            normal: {
                                show: true,
                                position: "top",
                                formatter: "{c}",
                                color: '#fff'
                            }
                        },
                        data: Response.y_list,
                        // animationDuration: function (idx) {
                        //     return idx * 1500 + 1000;
                        // }
                    }
                    ]
                };
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();
                });


            }
        });


    }


    function echarts_4() {

        // 取数据
        $.ajax({
            url: "/api/echarts4",
            type: 'GET',
            async: false,
            success: function (Response) {

                // 基于准备好的dom，初始化echarts实例
                var myChart = echarts.init(document.getElementById('echarts4'));
                var myColor = ['#eb2100', '#eb3600', '#d0570e', '#d0a00e', '#34da62', '#00e9db', '#00c0e9', '#0096f3'];
                option = {

                    grid: {
                        left: '2%',
                        top: '1%',
                        right: '5%',
                        bottom: '0%',
                        containLabel: true
                    },
                    xAxis: [{
                        show: false,
                    }],
                    yAxis: [{
                        axisTick: 'none',
                        axisLine: 'none',
                        offset: '7',
                        axisLabel: {
                            textStyle: {
                                color: 'rgba(255,255,255,.6)',
                                fontSize: '14',
                            }
                        },
                        data: Response.x_list

                    }, {
                        axisTick: 'none',
                        axisLine: 'none',
                        axisLabel: {
                            textStyle: {
                                color: 'rgba(255,255,255,.6)',
                                fontSize: '14',
                            }
                        },
                        data: Response.y_list

                    }, {
                        name: '单位：件',
                        nameGap: '50',
                        nameTextStyle: {
                            color: 'rgba(255,255,255,.6)',
                            fontSize: '16',
                        },
                        axisLine: {
                            lineStyle: {
                                color: 'rgba(0,0,0,0)'
                            }
                        },
                        data: [],
                    }],
                    series: [{
                        name: '条',
                        type: 'bar',
                        yAxisIndex: 0,
                        data: Response.bl_list,
                        label: {
                            normal: {
                                show: true,
                                position: 'right',
                                formatter: function (param) {
                                    return param.value + '%';
                                },
                                textStyle: {
                                    color: 'rgba(255,255,255,.8)',
                                    fontSize: '12',
                                }
                            }
                        },
                        barWidth: 15,
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(1, 0, 0, 0, [{
                                    offset: 0,
                                    color: '#03c893'
                                },
                                    {
                                        offset: 1,
                                        color: '#0091ff'
                                    }
                                ]),
                                barBorderRadius: 15,
                            }
                        },
                        z: 2
                    }, {
                        name: '白框',
                        type: 'bar',
                        yAxisIndex: 1,
                        barGap: '-100%',
                        data: [99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5, 99.5],
                        barWidth: 15,
                        itemStyle: {
                            normal: {
                                color: 'rgba(0,0,0,.2)',
                                barBorderRadius: 15,
                            }
                        },
                        z: 1
                    }]
                };

                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();
                });

            }
        });


    }


    function echarts_6() {

        $.ajax({
            url: "/api/ciyun",
            type: 'GET',
            async: false,
            success: function (Response) {

                var myChart = echarts.init(document.getElementById("echarts6"));
                JosnList = [
                    {"name": "傻狗", "value": 233},
                    {"name": "傻猫", "value": 233},
                    {"name": "傻猪", "value": 233}
                ];
                option = {
                    tooltip: {
                        show: true,
                    },

                    series: [
                        {
                            type: 'wordCloud',
                            //size: ['9%', '99%'],
                            sizeRange: [14, 50],
                            //textRotation: [0, 45, 90, -45],
                            rotationRange: [-45, 90],
                            shape: 'circle',
                            textPadding: 0,
                            width: '80%',
                            // 画布高
                            height: '80%',
                            autoSize: {
                                enable: true,
                                minSize: 6,
                            },
                            textStyle: {
                                normal: {
                                    color: function () {
                                        return (
                                            'rgb(' +
                                            [Math.round(Math.random() * 256), Math.round(Math.random() * 256), Math.round(Math.random() * 256)].join(
                                                ','
                                            ) +
                                            ')'
                                        );
                                    },
                                },
                                emphasis: {
                                    shadowBlur: 2,
                                    shadowColor: '#333',
                                },
                            },
                            data: JosnList,
                        },
                    ],
                };
                // 使用刚指定的配置项和数据显示图表。
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();
                });

            }
        });



    }

    function pe01() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('pe01'));
        var txt = 81
        option = {
            title: {
                text: txt + '%',
                x: 'center',
                y: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    color: '#fff',
                    fontSize: '18'
                }
            },
            color: 'rgba(255,255,255,.3)',

            series: [{
                name: 'Line 1',
                type: 'pie',
                clockWise: true,
                radius: ['65%', '80%'],
                itemStyle: {
                    normal: {
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    }
                },
                hoverAnimation: false,
                data: [{
                    value: txt,
                    name: '已使用',
                    itemStyle: {
                        normal: {
                            color: '#eaff00',
                            label: {
                                show: false
                            },
                            labelLine: {
                                show: false
                            }
                        }
                    }
                }, {
                    name: '未使用',
                    value: 100 - txt
                }]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function pe02() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('pe02'));
        var txt = 17
        option = {
            title: {
                text: txt + '%',
                x: 'center',
                y: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    color: '#fff',
                    fontSize: '18'
                }
            },
            color: 'rgba(255,255,255,.3)',

            series: [{
                name: 'Line 1',
                type: 'pie',
                clockWise: true,
                radius: ['65%', '80%'],
                itemStyle: {
                    normal: {
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    }
                },
                hoverAnimation: false,
                data: [{
                    value: txt,
                    name: '已使用',
                    itemStyle: {
                        normal: {
                            color: '#ea4d4d',
                            label: {
                                show: false
                            },
                            labelLine: {
                                show: false
                            }
                        }
                    }
                }, {
                    name: '未使用',
                    value: 100 - txt
                }]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function pe03() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('pe03'));
        var txt = 2
        option = {
            title: {
                text: txt + '%',
                x: 'center',
                y: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    color: '#fff',
                    fontSize: '18'
                }
            },
            color: 'rgba(255,255,255,.3)',

            series: [{
                name: 'Line 1',
                type: 'pie',
                clockWise: true,
                radius: ['65%', '80%'],
                itemStyle: {
                    normal: {
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    }
                },
                hoverAnimation: false,
                data: [{
                    value: txt,
                    name: '已使用',
                    itemStyle: {
                        normal: {
                            color: '#395ee6',
                            label: {
                                show: false
                            },
                            labelLine: {
                                show: false
                            }
                        }
                    }
                }, {
                    name: '未使用',
                    value: 100 - txt
                }
                ]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

    function pe04() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('pe04'));
        var txt = 2
        option = {
            title: {
                text: txt + '%',
                x: 'center',
                y: 'center',
                textStyle: {
                    fontWeight: 'normal',
                    color: '#fff',
                    fontSize: '18'
                }
            },
            color: 'rgba(255,255,255,.3)',

            series: [{
                name: 'Line 1',
                type: 'pie',
                clockWise: true,
                radius: ['65%', '80%'],
                itemStyle: {
                    normal: {
                        label: {
                            show: false
                        },
                        labelLine: {
                            show: false
                        }
                    }
                },
                hoverAnimation: false,
                data: [{
                    value: txt,
                    name: '已使用',
                    itemStyle: {
                        normal: {
                            color: '#395ee6',
                            label: {
                                show: false
                            },
                            labelLine: {
                                show: false
                            }
                        }
                    }
                }, {
                    name: '未使用',
                    value: 100 - txt
                }
                ]
            }]
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
})



		
		
		


		



















