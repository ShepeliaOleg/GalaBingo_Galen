@objects
       login-button           xpath   //*[contains(@class,'btn btn_action_login fr fn-login')]
       join_now-button        xpath   //*[contains(@class, 'btn btn_action_register fr')]
       logo                   xpath   //*[contains(@class,'main-logo')]
       container-header       xpath   //div[contains(@class, 'main-header')]
       menu-mobile            xpath   //*[contains(@class, 'main-header__menu fn-open-menu open-menu_btn left-header-block')]

       banner                 id      column-1
       
= Header =

    @on mobile
        logo:
             height 65px
             width  65px
             near join_now-button -32 to 44px right
             inside container-header 5px top
             
        menu-mobile:
              height 45px
              width  45px
              inside container-header

        join_now-button:
              width 79px
              height 45px
              text is "Join Now"
              inside container-header 0px right
              inside logo 95 to 100px left
              inside container-header
              color-scheme 80 to 100% #ec028d

        container-header:
              width 300 to 420px
              height 45px

= Banner =

    @on mobile
        banner:
              height 149px
              width  300 to 400px