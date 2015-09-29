@objects
       login-button           xpath   //*[contains(@class,'btn btn_action_login fr fn-login')]
       logo                   xpath   //*[contains(@class,'main-header__logo')]
       menu-item-*            xpath   //*[contains(@class, 'menu__nav fn-nav')]/li
       menu-bingo             xpath   //*[contains(@class, 'menu__nav fn-nav')]/li[contains(text(), 'Galabingo')]
       menu-slots             xpath   //*[contains(@class, 'menu__nav fn-nav')]/li[contains(text(), 'My Account')]
       menu-vegas             xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Vegas')]
       menu-promos            xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Promos')]
       menu-flutter           xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Flutter')]
       menu-cashback          xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Cashback')]
       menu-happy             xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Happy')]
       menu-clubs             xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'Clubs')]
       menu-vip               xpath   //*[contains(@class, 'header-navigation-primary')]/li/a[contains(text(), 'VIP')]

= Header =
    @on desktop
        logo:
              height 108px
              width  106px
              near login-button -900 to -955px right
        
        menu-bingo:
             aligned horizontally all menu-slots
