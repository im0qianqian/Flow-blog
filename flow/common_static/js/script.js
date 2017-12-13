console.log("\n %c 欢迎来到 https://www.dreamwings.cn 站长：千千  %c 继续踏上旅途，在没有你的春天…… by imqxms. \n\n", "color: #ffff00; background: #9999ff; padding:5px 0;", "background: #fadfa3; padding:5px 0;");

/* 标题栏 */
var OriginTitile = document.title,titleTime;
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
		$('[rel="shortcut icon"]').attr("href", "//www.dreamwings.cn/wp-content/uploads/2016/05/fail.ico");
		document.title = '(●—●)喔哟，崩溃啦！';
        clearTimeout(titleTime);
    }
else {
		$('[rel="shortcut icon"]').attr("href", "//www.dreamwings.cn/wp-content/uploads/2016/08/favicon32.ico");
		document.title = '(/≧▽≦/)咦！又好了！ ' + OriginTitile;
        titleTime = setTimeout(function() {
            document.title = OriginTitile;
        }, 2000);
    }
});


/* 积分特效 */
$("html,body").click(function(e) {
    var n = Math.round(Math.random() * 100);
    var $i = $("<b/>").text("+" + n);
    var x = e.pageX,
    y = e.pageY;
    $i.css({
        "z-index": 99999,
        "top": y - 20,
        "left": x,
        "position": "absolute",
        "color": "#"+("00000"+((Math.random()*16777215+0.5)>>0).toString(16)).slice(-6) //"#E94F06" 随机颜色
    });
    $("body").append($i);
    $i.animate({
        "top": y - 180,
        "opacity": 0
    },
    1500,
    function() {
        $i.remove();
    });
    e.stopPropagation();
});