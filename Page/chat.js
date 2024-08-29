<!-- Messenger Chat Plugin Code -->
    <div id="fb-root"></div>

    <div id="fb-customer-chat" class="chat"></div>
    
    <script>
      var chatbox = document.getElementById('zeta-chat');
      chatbox.setAttribute("405970549066637", "405970549066637");
      chatbox.setAttribute("attribution", "message_inbox");
    </script>


    <script>
      window.fbAsyncInit = function() {
        FB.init({
          xfbml            : true,
          version          : '2'
        });
      };

      (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = 'https://connect.facebook.net/en_US/sdk/xfbml.customerchat.js';
        fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));
    </script>
