import sublime_plugin

import functools as ftools


class JoinLinesLightCommand(sublime_plugin.TextCommand):
        
    def run(self, edit):
        
        def concatenate(string, nextstr):
            if string == "":
                return nextstr
            elif nextstr == "":
                return string
            else:
                sp = "" if string.endswith(("(", "[", "{", "<")) else " "
                return string + sp + nextstr

        vw = self.view

        for rgn in vw.sel():

            tgtrgn = vw.line(vw.full_line(rgn))
            lines = iter(vw.substr(tgtrgn).splitlines())
            firstline = next(lines).rstrip()
            stripped = (line.strip()  for line in lines)

            joined = ftools.reduce(concatenate, stripped, firstline)
            vw.replace(edit, tgtrgn, joined)
