alfred_snippets
===============

Simple, document-specific text snippets


### Version: 1.0
 
Download on Packal

 
 
 
Have you ever been taking notes and realized that certain terms or phrases were going to be used repeatedly? You don't have the time or really the desire to create all new TextExpander snippets for these terms or phrases, but you'd also really like to shorten your typing. That's where `Snippets` comes in. `Snippets` is a dead simple Alfred workflow that allows you to use simple snippet syntax while writing, and then seamlessly convert your text to its full glory.

The set-up is simple. As you're typing, and you realize you want to make a snippet, simply prepend your snippet with `,,` (comma comma). Then, when you get a free moment, create a "snippet dictionary" to tell Snippets what that snippet means. To create the dictionary, simply wrap it in `^^^` (triple carets). Here's an example:
```
This is an example of ,,sn. ,,sn is a fantastic workflow for ,,a!

^^^
sn: `Snippets`
a: Alfred
^^^
```
That's all there is to it. Once your dictionary is complete and you have finished typing, either copy the text to the clipboard and use the keyword `snip`, or assign a keyboard shortcut for even quicker results. When you activate `Snippets`, the text above will instantly become:
```
This is an example of `Snippets`. `Snippets` is a fantastic workflow for Alfred!
```
It's so simple. Double-comma before the snippet; dictionary wrapped in triple-carets with snippet: expanded. Nothing more, nothing less.

Hope this helps,
stephen
