    $(document).ready(function() {
        
            var d = new Date();
            var milTime = d.getHours();
            if (milTime < 12) {
                $('#p-after-greeting').prepend("Good morning! ");
            }
            else if (milTime < 18) {
                $('#p-after-greeting').prepend("Good afternoon! ");
            }
            else {
                $('#p-after-greeting').prepend("Good evening! ");
            }
  
        $('#show-about-me').click(
            function() {
                $('#about-me').show().siblings().hide();
            });
    
        $('#show-experience').click(
            function() {
                $('#experience').show().siblings().hide();
            });
        
        $('#show-education').click(
            function() {
                $('#education').show().siblings().hide();
            });
        
        $('#show-skills').click(
            function() {
                $('#skills').show().siblings().hide();
            });
        
        $('#show-professional').click(
            function() { 
                $('#professional').show().siblings().hide();
            });
        
        $('#show-portfolio').click(
            function() {
                $('#portfolio').show().siblings().hide();
            });

        $('#show-contact-me').click(
            function() {
                $('#contact-me').show().siblings().hide();
            });
                
        $('.accordion').find('.accordion-toggle').click(
            function(){
                $(this).next().slideToggle();
        });     
     
    });