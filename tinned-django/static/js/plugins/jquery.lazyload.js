(function($) {

    $.fn.lazyload = function(options) {
        var settings = {
            threshold    : 0,
            failurelimit : 0,
            container    : window,
            data_attr_mapping : {img: 'src', span: 'style'}
        };
        if(options) {
            $.extend(settings, options);
        }

        var lazyloadBlock = false;
        var lazyloadScrollTop;
        var elements = this;
        var scroll_handler = function(){
            // Проверка на то, что после таймаута произошло смещение
            if ($(window).scrollTop() === lazyloadScrollTop) {
                return;
            }
            lazyloadScrollTop = $(window).scrollTop();

            var counter = 0;
            elements.each(function() {
                if ($.abovethetop(this, settings) ||
                    $.leftofbegin(this, settings)) {
                        /* Nothing. */
                } else if (!$.belowthefold(this, settings) &&
                    !$.rightoffold(this, settings)) {
                        $(this).trigger('appear');
                } else {
                    if (counter++ > settings.failurelimit) {
                        return false;
                    }
                }
            });
            /* Remove image from array so it is not looped next time. */
            var temp = $.grep(elements, function(element) {
                return !element.loaded;
            });
            elements = $(temp);
        };
        $(settings.container).bind('scroll', function() {
            // Блокируем скролл во избежании перегруза
            if (lazyloadBlock) {
                return;
            }
            lazyloadBlock = true;
            setTimeout(function(){
                lazyloadBlock = false;
                scroll_handler();
            }, 500);
            scroll_handler();
        });

        this.each(function() {
            var self = this;
            $(self).one('appear', function() {
                var attrName = settings.data_attr_mapping[this.tagName.toLowerCase()];
                $(this).attr(attrName, $(self).data(attrName));
                this.loaded = true;
            });
        });

        /**
         * Форсируем начальную проверку
         */
        $(settings.container).trigger('scroll');

        return this;
    };


    $.belowthefold = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $(window).height() + $(window).scrollTop();
        } else {
            var fold = $(settings.container).offset().top + $(settings.container).height();
        }
        return fold <= $(element).offset().top - settings.threshold;
    };
    $.rightoffold = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $(window).width() + $(window).scrollLeft();
        } else {
            var fold = $(settings.container).offset().left + $(settings.container).width();
        }
        return fold <= $(element).offset().left - settings.threshold;
    };
    $.abovethetop = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $(window).scrollTop();
        } else {
            var fold = $(settings.container).offset().top;
        }
        return fold >= $(element).offset().top + settings.threshold  + $(element).height();
    };
    $.leftofbegin = function(element, settings) {
        if (settings.container === undefined || settings.container === window) {
            var fold = $(window).scrollLeft();
        } else {
            var fold = $(settings.container).offset().left;
        }
        return fold >= $(element).offset().left + settings.threshold + $(element).width();
    };
    $.extend($.expr[':'], {
        "below-the-fold" : "$.belowthefold(a, {threshold : 0, container: window})",
        "above-the-fold" : "!$.belowthefold(a, {threshold : 0, container: window})",
        "right-of-fold"  : "$.rightoffold(a, {threshold : 0, container: window})",
        "left-of-fold"   : "!$.rightoffold(a, {threshold : 0, container: window})"
    });

})(jQuery);