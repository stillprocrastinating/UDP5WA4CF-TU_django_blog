# Posts

|Key|Name|Type|Unique|
|-|-|-|-|
||Title|Char(200)||
||Slug|SlugField|:white_check_mark:|
|ForeignKey|Author|User model||
||Content|TextField||
||Created_on|DateTimeField||
||Status|Integer||
||Excerpt|TextField||
||Updated_on|DateTimeField||


# Comments

|Key|Name|Type|Unique|
|-|-|-|-|
|ForeignKey|Post|Post model||
|ForeignKey|Author|User model||
||Body|TextField||
||Approved|BooleanField||
||Created_on|DateTimeField||

