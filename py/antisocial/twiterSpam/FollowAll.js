var FOLLOW_PAUSE = 1250;
var FOLLOW_RAND = 250;
var PAGE_WAIT = 2000;
__cnt__ = 0;
var f;
f = function() {
        var eles;
        var __lcnt__ = 0;
        eles = jQuery('.Grid-cell .not-following .follow-text').each(function(i, ele) {
                    ele = jQuery(ele);
                    if (ele.css('display') != 'block') {
                        console.trace('Already following: ' + i);
                        return;
                    }
                    setTimeout(function() {
                              console.trace("Following " + i + " of " + eles.length);
                            ele.click();
                            if ((eles.length - 1) == i) {
                                console.trace("Scrolling...");
                                window.scrollTo(0, document.body.scrollHeight);
                                setTimeout(function() {
                                    f();
                                }, PAGE_WAIT);
                            }
                    }, __lcnt__++ * FOLLOW_PAUSE + Math.random()*(FOLLOW_RAND) - FOLLOW_RAND/2);
                    __cnt__++;
        });
}
f();
