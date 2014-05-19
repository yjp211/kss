

$(document).ready(function(){

    /**
     * 绑定顶部菜单点击事件，切换TAB
     * return： false
     */
    $(".menu .menu-link").bind('click', function(){
        var dest_url = $(this).attr('href');

        //loop iframe
        $("iframe").each(function(){
           var data_url = $(this).attr('data-url');
            if(dest_url == data_url){
                // load the page when first open
                if($(this)[0].src != data_url){
                    $(this)[0].src = data_url;
                }
                // show this frame
                $(this).removeClass('frame-hidden');
                $(this).addClass('frame-display');
            }else{
                $(this).removeClass('frame-display');
                $(this).addClass('frame-hidden');
            }
        });

        return false;
    })
});