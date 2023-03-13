import sublime_plugin

import functools as ftools


class JoinLinesLightCommand(sublime_plugin.TextCommand):
        
    def run(self, edit):
        
        def addstr(string, nextstr):
            if string == "":
                return nextstr
            elif nextstr == "":
                return string
            else:
                sp = "" if string.endswith(("(", "[", "{", "<")) else " "
                return string + sp + nextstr

        vw = self.view

        for rgn in vw.sel():
            linergns = vw.lines(rgn)
            lastline = vw.line(linergns[-1].end() + 1)
            linergns.append(lastline)
            strings = map(vw.substr, linergns)
            firstlinestr = next(strings).rstrip(" \t")
            stripped = (strg.strip(" \t")  for strg in strings)

            joined = ftools.reduce(addstr, stripped, firstlinestr)
            exrgn = linergns[0].cover(linergns[-1])
            vw.replace(edit, exrgn, joined)
