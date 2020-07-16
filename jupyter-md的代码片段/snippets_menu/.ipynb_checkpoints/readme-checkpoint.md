Jupyter笔记本片段菜单
==============================

向Jupyter笔记本添加可自定义的菜单项以插入代码段，样板和代码示例。

![Open snippets menu](screenshot1.png)

此笔记本扩展会添加一个菜单项（或多个菜单项，如果在Jupyter笔记本的“帮助”菜单之后。这个新菜单包含一些我们不时忘记的小片段代码但不想谷歌，或者太懒了而无法输入，或者只是不知道对于刚开始的人们也有帮助用一种编程语言，他们需要一些有关做什么的想法下一步-
诸如导入模块，定义变量或调用功能。新菜单带有与python相关的默认值程序设计-尤其是科学计算-
尽管这完全用户可配置，如下所述。默认菜单名为“片段”，其中包含带有一些流行片段的子菜单python软件包，python本身以及一些笔记本降价促销。（请注意，某些菜单太大，因此必须移动左侧的一级菜单，以便较低一级的菜单适合屏幕上。如前所述，此行为也是用户可配置的详细地
[below](#change-direction-of-sub-menus).)

因此，例如，如果您正在编辑代码单元并想要导入用于笔记本的matplotlib，您只需单击“片段”菜单，然后将鼠标悬停在“
Matplotlib”上。这将打开一个新的子菜单，带有“笔记本设置”项目。点击该项目将插入光标在您之前的位置的代码段在菜单上单击。特别是对于这个“
matplotlib”示例，插入以下代码：

```{.python .input}
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
```

插入的文本将被选中，以便您可以通过以下方式将其删除按Backspace键或Delete键，或者您可以选择另一个代码段替换它-
只是突出显示插入的内容。请注意，许多摘录都包含以前缀的变量名bp_。例如，一个新的numpy数组被创建为“
bp_new_array”。这些是您确实应该替换的哑巴名称。如果不这样做，可能会导致代码中的丑陋错误变量名冲突的多个样板摘要。同样，某些字符串也打算替换，例如轴地块中的标签。这些是为了向您展示可以做什么，以及提醒您在地块上贴上信息丰富的标签。如果你不这样做想要例如地块上的标题，只需删除该行。


安装
------------
要单独安装此扩展（不安装[nbextensions的主要集合]
（https://github.com/ipython-contrib/jupyter_contrib_nbextensions））
，请从命令行运行以下命令：

```{.python .input}
git clone git://github.com/moble/jupyter_boilerplate
jupyter nbextension install jupyter_boilerplate
jupyter nbextension enable jupyter_boilerplate/main
```

然后，您可以根据需要禁用扩展名

```{.python .input}
jupyter nbextension disable jupyter_boilerplate/main
```

基本菜单定制
------------------------

默认菜单可能包含太多与您无关的项目，或者没有您会觉得有用的东西。您可以轻松自定义它在里面
[jupyter_nbextensions_configurator](https://github.com/Jupyter-
contrib/jupyter_nbextensions_configurator#usage),
如果您安装了此扩展程序，几乎可以肯定正常的方式通过
[jupyter_contrib_nbextensions](https://github.com/ipython-
contrib/jupyter_contrib_nbextensions).
通常，您可以通过将浏览器指向
http://127.0.0.1:8888/nbextensions, 尽管您可能需要修改如果使用更复杂的jupyter服务器，则为URL。

在配置器页面上，您将看到许多选项（以及本自述文件）应该是不言自明的，允许您删除任何默认菜单项，或在“摘要”菜单。自定义菜单是用JSON编写的，（且无用）给出的示例应易于修改为需要。



高级菜单定制
---------------------------

还可以广泛地自定义菜单使用您的custom.js文件的复杂方式。例如，您可以更改菜单项的顺序，在下面添加更多自定义子菜单“代码段”菜单，以及菜单中“代码段”旁边的自定义菜单栏，甚至在其他位置添加菜单，例如“插入”菜单中的菜单。
通过命令行找到以下路径
`custom.js`

```{.python .input  n=1}
echo $(jupyter --config-dir)/custom/custom.js
```

```{.json .output n=1}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "$(jupyter --config-dir)/custom/custom.js\n"
 }
]
```

For Mac and linux users, the result is probably
`~/.jupyter/custom/custom.js`.  If this file or the directory
containing it do not exist, you can simply create them.

The customization process is best explained through examples, which
are available in the `examples_for_custom.js` file in this directory.
Note that there's a lot of explanation here, but it's all actually
pretty simple.  Give it a try, and you'll pick it up quickly.  Note
that using this method can make it so that options selected in the
configurator are ignored.

The theory behind this customization is that the menu is represented
by a nested JavaScript array (which is just like a python list).  So
to change the menu, you just need to change that array.  And each menu
*item* inside this array is represented by
a [JavaScript "object"](https://api.jquery.com/Types/#Object) (which is
just like a python dictionary).  So to change a menu item, you just
have to change that object.

Again, this makes more sense when looking at example, as follows.


### Add a custom sub-menu with simple snippets

Suppose you want to make a new sub-menu with your favorite snippets at
the bottom of `Snippets`.  You create a new object for the menu item,
and then just "push" it onto the default menu.  Do this by inserting
some lines into your `custom.js`, so that it looks like this:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    var horizontal_line = '---';
    var my_favorites = {
        'name' : 'My favorites',
        'sub-menu' : [
            {
                'name' : 'Menu item text',
                'snippet' : ['new_command(3.14)',],
            },
            {
                'name' : 'Another menu item',
                'snippet' : ['another_new_command(2.78)',],
            },
        ],
    };
    snippets_menu.options['menus'] = snippets_menu.default_menus;
    snippets_menu.options['menus'][0]['sub-menu'].push(horizontal_line);
    snippets_menu.options['menus'][0]['sub-menu'].push(my_favorites);
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

Now, if you refresh your notebook, you'll see a new menu item named "My
favorites".  Hover over it, and it will pop up a sub-menu with two more
options.  Click the first one, and it will insert `new_command(3.14)` into
your notebook wherever the cursor was.

We discuss how all this works below.  But first, we need to slightly generalize
the example above to work with more complicated snippets.


### More complicated snippets

The example above inserted simple one-line snippets of code.  Those snippets
didn't have any quotation marks (single or double), backslashes, or newlines,
which made everything easy.  Unfortunately, JavaScript doesn't deal too well
with strings.  (There are no raw triple-quoted strings, like in python.)  So
there are just three things to remember when writing snippets.

  1. Quotation marks can be a tiny bit tricky.  There are a few options:
    1. The obvious option is to enclose your snippets in single quotation marks
       (`'`), and use only double quotation marks (`"`) within the snippet
       itself.
    2. Just as easy is to enclose your snippets in double quotation marks
       (`"`), and use only single quotation marks (`'`) within the snippet
       itself.
    3. You can also escape single quotation marks inside single quotation marks
       as `\'`.

  2. Newlines are even trickier, but the extension takes care of this for you
     as long as you put separate lines of code as separate elements of the
     `snippet` array.  Generally, there's no reason to put a literal newline in
     your snippets.

  3. JavaScript will treat backslashes as if they're trying to escape whatever
     comes after them.  So if you want one backslash in your output code,
     you'll need to put two backslashes in.

This is all best described with another example.  Let's change the first
function above, to give it some more lines and some quotes:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    var horizontal_line = '---';
    var my_favorites = {
        'name' : 'My $\\nu$ favorites',
        'sub-menu' : [
            {
                'name' : 'Multi-line snippet',
                'snippet' : ['new_command(3.14)',
                             'other_new_code_on_new_line("with a string!")',
                             'stringy(\'escape single quotes once\')',
                             "stringy2('or use single quotes inside of double quotes')",
                             'backslashy("This \\ appears as just one backslash in the output")',
                             'backslashy2("Here are \\\\ two backslashes")',],
            },
            {
                'name' : 'TeX appears correctly $\\alpha_W e\\int_0 \\mu \\epsilon$',
                'snippet' : ['another_new_command(2.78)',],
            },
        ],
    };
    snippets_menu.options['menus'].push(snippets_menu.default_menus[0]);
    snippets_menu.options['menus'][0]['sub-menu'].push(horizontal_line);
    snippets_menu.options['menus'][0]['sub-menu'].push(my_favorites);
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

Note the code output by the first item contains all sorts of interesting
strings.  Also, the menu title of the second item contains TeX, which will
display correctly, and is used in some of the default menus to show the
standard symbols for physical constants.  For more examples, look at the
default menus stored in the `snippets_menu` directory -- mostly under `python`.


### How it works: Creating new menu items

Each of the menu items above is a JavaScript object (like a python `dict`),
with some attributes -- `name` and `sub-menu` for the main menu item, and
`name` and `snippet` for the sub-menu items.  In general, any menu object can
have any of the following properties:

  1. `name`: Text that appears in the menu.  Note that this can include latex,
     as the menus are processed by MathJax after being loaded.
  2. `sub-menu`: An array of more menu items
  3. `snippet`: An array of strings turned into code when the menu item is
     clicked
  4. `internal-link`: Link to some place on the present page.  For example,
     this could be `#References`, to link to the `References` section of any
     notebook you're in.
  5. `external-link`: This just a link to some external web page, which will be
     identified with a little icon, just like in the standard notebook "Help"
     menu.  When clicked, the link will open in a new window/tab.
  6. `menu-direction`: If the value of this property is `left`, this menu's
     sub-menus open on the left.  This is useful when the top-level menu is
     inserted as an item within other menu items.  See
     [below](#change-direction-of-sub-menus) for examples.
  7. `sub-menu-direction`: If the value of this property is `left`, sub-menus
     within this menu's sub-menus open on the left.  This is used by default
     for items under the `Snippets` menu to help ensure that nested menus
     don't become too large to fit on the screen.  See
     [below](#change-direction-of-sub-menus) for examples.

The `name` property is the only required one, though you'll probably want at
least one other property.  The `sub-menu` contains menu objects that again may
have any of these properties, so you can easily nest menus.  You can also
combine a `snippet` with a `sub-menu`, so that there's a default value as well
as a sub-menu.  However, the last three are mutually exclusive: `snippet` will
override any `-link`; an `internal-link` will override an `external-link`.


### How it works: Splicing new menu items into the old

Besides just creating the menu items, we may want to join together previously
created items.  That's the purpose of this line in the code above:

```{.python .input .javascript}
    snippets_menu.options['menus'][0]['sub-menu'].push(my_favorites);
```

This uses
the [JavaScript `push`](https://www.w3schools.com/jsref/jsref_push.asp)
function to insert the new menu `my_favorites` menu into the last slot
of `snippets_menu.options['menus'][0]['sub-menu']`, which is the set
of menus under the heading `Snippets`.

If you think about this last point, you'll realize that `Snippets` is
just the `0` slot of an array of menus.  If you want a new menu right
in the menu bar, you could add `my_favorites` right to that top-level
array, with something like this:

```{.python .input .javascript}
    snippets_menu.options['menus'].push(snippets_menu.default_menus[0]);
    snippets_menu.options['menus'].push(my_favorites);
```

This would place your favorites after the default `Snippets` menu; to
put it before, just swap the order in which you `push`:

```{.python .input .javascript}
    snippets_menu.options['menus'].push(my_favorites);
    snippets_menu.options['menus'].push(snippets_menu.default_menus[0]);
```

(In general, to add a new element at a given index of an array, you
could also just use
the [splice](https://www.w3schools.com/jsref/jsref_splice.asp)
function.)

This might be useful if you have one set of very frequently used
commands, and want immediate access, without going through various
levels of the usual menu.  A useful example of this is
shown [below](#starting-over-with-the-menus).  The `splice` function
can also be used to delete items from the array, as
described [next](#deleting-menu-items).


### Other menu manipulations

To rearrange menu items, just use standard JavaScript techniques.  The two most
likely examples are deleting and rearranging menu items, but we'll also see
that other manipulations are easy.  We can also change where the new menus go,
and what they look like.

#### Deleting menu items

To delete an item, just `splice` nothing into it.  Let's suppose, for example,
that you want to remove the option to set up matplotlib for a script, which is
the `1` item of the "Matplotlib" menu:

```{.python .input .javascript}
snippets_menu.python.matplotlib['sub-menu']
```

Remember that `[1]` is the second element of "Matplotlib"'s sub-menu
list.  So the following code will do the trick

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    snippets_menu.python.matplotlib['sub-menu'].splice(1, 1); // Delete 1 element starting at position 1 of the sub-menu
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

The first `1` in the argument to `splice` says to work on the element at
position 1; the second `1` says to delete 1 element of the array.


#### Rearranging menu items

Following the example above, suppose you don't want to delete the second setup
item under "Matplotlib", but instead want to swap those first two items.  To
make this swap, you need to do the usual trick of storing one element in a
temporary variable, and then reassign appropriately.  The following code
achieves this purpose:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    var tmp = snippets_menu.python.matplotlib['sub-menu'][0];
    snippets_menu.python.matplotlib['sub-menu'][0] = snippets_menu.python.matplotlib['sub-menu'][1];
    snippets_menu.python.matplotlib['sub-menu'][1] = tmp;
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

#### Change direction of sub-menus

Each sub-menu may be placed to the right or left side of the menu item
containing it.  This is controlled by the `menu-direction` and
`sub-menu-direction` properties of the container.  By default, both are set to
`right` for all menus, but `sub-menu-direction` is set to `left` for the
default `Snippets` menu, which means that all of its sub-menus open to the
left side.  This is important because the menus may be nested quite deeply, and
need to fit on the screen.  For example, the SciPy CODATA constants and SymPy's
orthogonal functions will easily extend far past the right-hand edge of the
notebook without this feature.  That means the window size would abruptly
increase when you mouse over these menus, and would abruptly collapse when you
mouse out of them.  So by opening them to the left, we gain enough space to
keep everything on the screen.

But these are configurable properties.  If, for example, you want to change the
default menus to open on the right (which would be the more standard behavior),
you can use this:

```{.python .input .javascript}
    snippets_menu.default_menus[0]['sub-menu-direction'] = 'right';
```

This may be particularly useful if we change the position of the menus, as in
the next examples.


#### Starting over with the menus

Each of the menu items under the default `Snippets` menu is
individually available as part of the `snippets_menu` object defined
in our JavaScript examples.  So if you want, you could just use them
to build your own version of the menu.  For example, suppose use SymPy
and Numpy most frequently, so you want easy access to their menus,
without having to click `Snippets` first.  And then suppose you still
want most of the other `Snippets` items, but less frequently so they
can stay in their menu, except that you really never use pandas.  You
can create your own menu as follows:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    snippets_menu.default_menus[0]['sub-menu'].splice(3, 2); // Remove SymPy and pandas
    snippets_menu.python.sympy['sub-menu-direction'] = 'left'; // Point new SymPy menus to left
    snippets_menu.python.numpy['sub-menu-direction'] = 'left'; // Point new Numpy menus to left
    snippets_menu.options['menus'].push(snippets_menu.default_menus[0]); // Start with the remaining "Snippets" menu
    snippets_menu.options['menus'].push(snippets_menu.python.sympy); // Follow that with a new SymPy menu
    snippets_menu.options['menus'].push(snippets_menu.python.numpy); // Follow that with a new Numpy menu
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

The default menu group is `snippets_menu.default_menus`, and the SymPy sub-menu
is `snippets_menu.python.sympy`.  You can see that we've manipulated them above
by removing two elements from the default menu, using the `splice` command.
We've also added a new property to the SymPy menu to make its sub-menus open to
the left, instead of the right -- which is necessary to keep all of SymPy's
extensively nested menus on the screen.  (In fact, the list of orthogonal
polynomials under "Special functions" in the SymPy menu are some of the widest
menus in the default set.)  Finally, we've combined the modified default menu
with the modified SymPy menu into one new list.

This gives us the original `Snippets` menu with SymPy and pandas removed, as
well as new menus devoted to just SymPy and Numpy right in the menu bar:

![Opened snippets menu after adjustments](screenshot2.png)

You can see that the two items are indeed removed from `Snippets`, and
"SymPy" and "Numpy" now have places of honor right in the menu bar.
You can, of course, swap their order in the code above, or make any
number of further alterations.


#### Changing the insertion point

You might want to change the order of the menus in the navbar (that
top-level bar with "File", etc.).  For example, it might feel
particularly natural to have "Help" as the last item, so maybe you'd
prefer to put the `Snippets` menu *before* the "Help" menu.  Or you
may prefer to maintain the structure of the menus in the navbar, and
would rather have the `Snippets` menu *inside* of some other top-level
menu -- like the "Insert" menu.  Personally, I prefer to have the
`Snippets` menu in its default position for easy access.  But it's
certainly possible to put it other places.

To help do this, there are two additional options available, which can
be set either in the configurator or in `custom.js`.  Their default
values give us the usual placement of the `Snippets` menu; by giving
them different values, we can change the placement.  These options are

  1. `sibling`: This is an HTML node next to our new menu,
     presumably
     [selected with `jQuery`](https://learn.jquery.com/using-jquery-
core/selecting-elements/).
     The default value is `$("#help_menu").parent()`, which is the
     "Help" menu.  For the configurator, `.parent()` is automatically
     appended.
  2. `insert_before_sibling`: This is just a string controlling where
     the new menu will be inserted relative to its sibling. The
     default value is `false`.  If you change it to `true`, the new
     menu will be inserted before the sibling.

So placing the `Snippets` menu *before* the "Help" menu is as easy as
checking the box for that second option.  For more complicated uses,
you may need to set these values from `custom.js`.  For example, f you
want to put the new `Snippets` menu as an item inside the standard
"Insert" menu, and include an additional horizontal divider, you can
use this:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    snippets_menu.default_menus[0]['menu-direction'] = 'left'; // Open top-level menu to the left...
    snippets_menu.default_menus[0]['sub-menu-direction'] = 'right'; // ...and sub-menus to the right.
    snippets_menu.options['menus'].push('---', snippets_menu.default_menus[0]); // Add horizontal line and default menus
    snippets_menu.options['sibling'] = $("#insert_cell_below"); // Find the place at which to insert the new menus
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

Here's what that looks like:

![Opened snippets menu under "Insert" menu](screenshot3.png)

And of course, you can combine this selection of the insertion point with other
techniques above, where you change the content of the menus.


#### Multiple menus in separate locations

Finally, we have one more interesting example that brings together various
threads from the previous examples.  It is possible to place multiple menus in
different locations.  For example, suppose we want to combine two of the
examples
above, where [(1)](#starting-over-with-the-menus) we separated "SymPy" into its
own menu on the navbar, and [(2)](#changing-the-insertion-point) we placed the
`Snippets` menu inside the "Insert" menu.  That is, you might want "SymPy"
to be conveniently placed, but you want the rest of the `Snippets` to stay
under the "Insert" menu.

To add these two separate menus, we place the first with the usual
approach, and then place the second with another function,
`snippets_menu.menu_setup`.  The former is mostly just a wrapper to
the latter, except that it also inserts JavaScript and CSS elements
into the notebook.  Note that `menu_setup` does not have any default
values; you must always pass the `sibling` and `insert_before_sibling`
arguments.

So, putting it all together, the code needed for this arrangement is as
follows:

```{.python .input .javascript}
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    var sympy_menu = [snippets_menu.python.sympy,];
    sympy_menu[0]['sub-menu-direction'] = 'left';
    snippets_menu.options['menus'] = sympy_menu;
    snippets_menu.default_menus[0]['sub-menu'].splice(3, 1); // Remove SymPy from defaults
    snippets_menu.default_menus[0]['menu-direction'] = 'left';
    snippets_menu.default_menus[0]['sub-menu-direction'] = 'right';
    var sibling = $("#insert_cell_below");
    var inserted_menu = [
        '---',
        snippets_menu.default_menus[0],
    ];
    snippets_menu.menu_setup(inserted_menu, sibling, 'after');
    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});
```

Troubleshooting
---------------

The first step is to make sure that the default setup can be loaded.
Comment out whatever you've got in `custom.js`, and add in the simple
configuration from [the beginning](#installation).  If that doesn't
work, try the following steps
suggested
[here](http://jupyter-contrib-
nbextensions.readthedocs.io/en/latest/troubleshooting.html):

  1. Clear your browser cache or start a private browser tab.
  2. Verify your `custom.js` is the one the notebook is seeing, by opening it
     in the browser: <http://127.0.0.1:8888/static/custom/custom.js> (as
     opposed to looking at the file directly outside of your browser, which may
     not be the `custom.js` loaded if you are using a `virtualenv`).
  3. Verify the extension can be loaded by the Jupyter notebook, for example:
     <http://127.0.0.1:8888/nbextensions/snippets_menu/main.js>.  You
     should see a page with lots of JavaScript code, and should *not*
     see a 404 error.
  4. Check for error messages in the JavaScript console.

Now, assuming the basic installation works, it must be something wrong
in your customization.  (Or maybe a new bug you've uncovered...)

Sometimes, the menu(s) might simply not appear.  This is most likely
due to a syntax error in your menu.  You can find out in Chrome by
going to "View" -> "Developer" -> "JavaScript console".  You'll see a
bunch of output.  Red lines are usually errors (some of which are
probably *not* due to your menu error).  On the right side of those
lines, you'll see the file where the error came from, and possibly
even the line number that's causing the trouble.  Find an error that
links to either `snippets_menu/main.js` or `custom.js`, and click on
it.  Then try to figure out what went wrong.  The most common error
I've encountered is "Unexpected string", which might indicate a
missing comma, or an improperly escaped quote.  Note that sometimes
the error will point to the first thing *after* the real problem.

Or maybe the menu did appear, but it doesn't work properly.  You can
also inspect the actual elements that were inserted.  Click on
"Elements" in that Developer Tools tab that opened at the bottom of
your window.  Then click the magnifying glass, and click on the
`Snippets` menu.  This will jump the Developer Tools to the part of
the source with that menu.  Scroll through to find the menu item
that's not working correctly, and take a look at it.  The text in the
`data-snippet-code` attribute is especially important, since that's
what gets inserted into the notebook.


TODO
----

There's a bunch of stuff I still need to do, listed in
the
[issue tracker](https://github.com/moble/jupyter_boilerplate/issues).
If you find a bug or have an idea for a good snippet that you think
should be added to the defaults, feel free
to
[open a new issue](https://github.com/moble/jupyter_boilerplate/issues/new).

In particular, I don't use Julia or R, so I welcome suggestions for
default snippets for those languages.



Reasons for using this extension
--------------------------------

This is just a nice place to collect thoughts about why anyone might
find this to be a useful extension:

  * Introducing beginners to coding.  It's helpful for the beginner to have a
    list of useful possibilities (with correct syntax!) lined up right where
    the programming is happening.  It's like "Hello world" on steroids.
  * Introducing the Jupyter notebook.  It can be useful to have some nice
    things to do in the notebook to demonstrate the possibilities.  For
    example, you might suggest that someone new to the notebook run the
    Matplotlib setup and then make an example plot.
  * Convenience for lazy people like me.  For example, I usually don't want to
    bother with all the typing involved in setting up the nice (but important)
    parts of a plot, like the axis labels and legend.  But by inserting the
    template, all I have to do is change the relevant values.
  * Reminders about useful things that could be done.  For example,
    when I'm manipulating expressions in SymPy, I'll frequently forget
    that I can simplify, expand, collect, etc., in all sorts of ways.
    The Snippets menu reminds me of that.
  * Convenient reference for massive libraries.  For example, SciPy contains
    lots of constants.  You could certainly go to the web page describing these
    various constants to find the one you need, or you could just explore them
    right in the browser.  The same is true of SymPy's collection of special
    functions.
