import random
import datetime
import sys


RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
RED    = "\033[31m"


# ---------------------------------------------------------------------------
# EXERCISES  (task, hint)
# ---------------------------------------------------------------------------

BEGINNER = [
    (
        "Move the cursor left, right, up, and down without using arrow keys.",
        "h (left)   l (right)   k (up)   j (down)"
    ),
    (
        "Jump forward and backward by one word at a time.",
        "w (next word start)   b (previous word start)   e (next word end)\n"
        "  Uppercase variants W / B / E treat whitespace as the only delimiter."
    ),
    (
        "Jump to the very beginning and very end of the current line.",
        "0 (column 0)   ^ (first non-whitespace char)   $ (end of line)"
    ),
    (
        "Jump to the first line and the last line of the file.",
        "gg (first line)   G (last line)"
    ),
    (
        "Jump to a specific line number — say, line 42.",
        ":42<Enter>   or   42G"
    ),
    (
        "Enter insert mode before the cursor, after the cursor, at the start "
        "of the line, and at the end of the line.",
        "i (before cursor)   a (after cursor)   I (line start)   A (line end)"
    ),
    (
        "Open a new line below the current line and enter insert mode. "
        "Then do the same above.",
        "o (new line below, insert)   O (new line above, insert)"
    ),
    (
        "Delete the character under the cursor. Then delete a whole line.",
        "x (delete char)   dd (delete line)"
    ),
    (
        "Delete from the cursor to the end of the current line.",
        "D   or   d$"
    ),
    (
        "Delete the word the cursor is on.",
        "dw (delete to next word boundary)   daw (delete word + surrounding space)"
    ),
    (
        "Undo your last change. Then redo it.",
        "u (undo)   Ctrl-r (redo)"
    ),
    (
        "Save the current file, then quit. Then quit without saving.",
        ":w (save)   :q (quit)   :wq or :x (save+quit)   :q! (quit without saving)"
    ),
    (
        "Copy (yank) the current line and paste it below, then above.",
        "yy (yank line)   p (paste below cursor/line)   P (paste above)"
    ),
    (
        "Enter character-wise visual mode, line-wise visual mode, and "
        "block visual mode.",
        "v (character)   V (line)   Ctrl-v (block)"
    ),
    (
        "Find the next occurrence of the letter 'e' on the current line "
        "and jump to it. Then jump backward to the previous one.",
        "f{char} (jump forward to char)   F{char} (backward)\n"
        "  t{char} / T{char} land one cell before/after\n"
        "  ; repeats the motion   , reverses it"
    ),
    (
        "Replace a single character under the cursor without entering insert mode.",
        "r{char}  — replaces the char under cursor and returns to normal mode"
    ),
    (
        "Change (delete + enter insert mode) from the cursor to the end of the line.",
        "C   or   c$"
    ),
    (
        "Change the word the cursor is sitting on.",
        "cw (change to next word boundary)   ciw (change inner word)"
    ),
    (
        "Repeat the last change you made.",
        ". (dot)  — replays the last normal-mode change"
    ),
    (
        "Jump to the bracket / paren / brace that matches the one under your cursor.",
        "% — bounces between matching (), [], {}"
    ),
    (
        "Scroll the screen so the current line is centered, at the top, "
        "and at the bottom — without moving the cursor.",
        "zz (center)   zt (top)   zb (bottom)"
    ),
    (
        "Scroll down and up by half a page, then a full page.",
        "Ctrl-d (half down)   Ctrl-u (half up)\n"
        "  Ctrl-f (full page down)   Ctrl-b (full page up)"
    ),
    (
        "Move the cursor to the top, middle, and bottom of the visible screen.",
        "H (high / top)   M (middle)   L (low / bottom)"
    ),
    (
        "Delete from the cursor to a specific character (exclusive).",
        "dt{char}  — deletes up to but not including {char} on the current line\n"
        "  ct{char} does the same but enters insert mode"
    ),
]


INTERMEDIATE = [
    (
        "Change the text inside a pair of double quotes, single quotes, "
        "parentheses, brackets, and curly braces — without deleting the delimiters.",
        'ci"  ci\'  ci(  ci[  ci{   (change INSIDE the delimiters)\n'
        "  Works from anywhere inside the pair — cursor doesn't need to be on the delimiter."
    ),
    (
        "Change the text inside a pair of delimiters AND delete the delimiters themselves.",
        'ca"  ca\'  ca(  ca[  ca{   (change AROUND — includes delimiters)'
    ),
    (
        "Yank (copy) the text inside parentheses into a named register, "
        "switch to another buffer, and paste it there.",
        '"ayi(  — yank inner parens into register a\n'
        "  :bn or Ctrl-^ to switch buffers\n"
        '  "ap  — paste from register a'
    ),
    (
        "Search forward in the file for a pattern, then navigate to the "
        "next and previous matches.",
        "/pattern<Enter> (forward search)   ?pattern<Enter> (backward)\n"
        "  n (next match)   N (previous match)"
    ),
    (
        "Search for the exact word the cursor is currently on.",
        "* (search forward for word under cursor)   # (search backward)\n"
        "  Both respect word boundaries."
    ),
    (
        "Replace every occurrence of a word in the whole file. "
        "Then do it with a confirmation prompt for each replacement.",
        ":%s/old/new/g   (replace all, no confirmation)\n"
        "  :%s/old/new/gc  (add 'c' flag — confirm each replacement)"
    ),
    (
        "Replace a word only within a visual selection.",
        "Select with V, then :s/old/new/g — the range '<,'> is filled automatically."
    ),
    (
        "Set a local mark on a line, move elsewhere, then jump back to "
        "the exact position of that mark.",
        "m{a-z}  — set a mark (e.g. ma)\n"
        "  `{a-z}  — jump to exact position of mark\n"
        "  '{a-z}  — jump to the line of the mark"
    ),
    (
        "Navigate backward through your jump history, then forward again.",
        "Ctrl-o (older jump / go back)   Ctrl-i (newer jump / go forward)\n"
        "  :jumps to see the full jump list"
    ),
    (
        "Navigate to a position where you recently made a change "
        "without using jump list.",
        "g; (go to older change)   g, (go to newer change)\n"
        "  :changes to see the full change list"
    ),
    (
        "Record a macro that adds a semicolon to the end of a line, "
        "then replay it on several lines.",
        "qa  — start recording into register a\n"
        "  A;<Esc>  — append semicolon, leave insert mode\n"
        "  q  — stop recording\n"
        "  @a  — replay   @@  — repeat last macro\n"
        "  5@a — replay 5 times"
    ),
    (
        "Edit a macro you already recorded (without re-recording it from scratch).",
        '"ap  — paste macro contents into buffer\n'
        "  Edit the text\n"
        '  "ayy  — yank the edited line back into register a\n'
        "  Alternatively: :let @a='<Ctrl-r a>' then edit inline"
    ),
    (
        "Split the current window horizontally, then vertically. "
        "Navigate between the splits.",
        ":sp or :split (horizontal)   :vs or :vsplit (vertical)\n"
        "  Ctrl-w h/j/k/l  — move between splits\n"
        "  Ctrl-w w  — cycle through splits\n"
        "  Ctrl-w =  — equalize split sizes"
    ),
    (
        "Open a file in a new split directly from the command line.",
        ":sp filename   :vs filename\n"
        "  Or from netrw: press o (horizontal) or v (vertical) on a file"
    ),
    (
        "List all open buffers, switch to a specific one, and close one.",
        ":ls or :buffers  — list buffers\n"
        "  :b{N}  — switch to buffer N   :bn / :bp  — next / previous\n"
        "  :bd  — delete (close) current buffer"
    ),
    (
        "Switch instantly to the file you were just editing (the alternate file).",
        "Ctrl-^  (or Ctrl-6)  — toggles between current and last-used buffer"
    ),
    (
        "Open netrw to browse the filesystem, navigate into a directory, "
        "and open a file.",
        ":Ex or :Explore  — opens netrw in current window\n"
        "  :Sex / :Vex  — horizontal / vertical split\n"
        "  Enter  — open file or directory   -  — go up one directory"
    ),
    (
        "Indent a line one level, dedent it, then indent a visual selection.",
        ">>  — indent line   <<  — dedent line\n"
        "  In visual mode: >  or  <\n"
        "  .  — repeat the indent/dedent"
    ),
    (
        "Auto-indent an entire function or block to fix its indentation.",
        "=  — auto-indent (takes a motion)\n"
        "  ==  — auto-indent current line\n"
        "  =G  — auto-indent from cursor to end of file\n"
        "  In visual mode: =  — auto-indent selection"
    ),
    (
        "Toggle the case of a character. Uppercase and lowercase a motion.",
        "~  — toggle case of char under cursor\n"
        "  gU{motion}  — uppercase (e.g. gUiw  — uppercase word)\n"
        "  gu{motion}  — lowercase\n"
        "  gUU / guu  — upper/lowercase entire line"
    ),
    (
        "Join the current line with the line below it.",
        "J  — joins next line with a space\n"
        "  gJ  — joins without adding a space"
    ),
    (
        "Open a new tab, switch between tabs, and close a tab.",
        ":tabnew  — new tab   :tabnew filename  — open file in new tab\n"
        "  gt  — next tab   gT  — previous tab   {N}gt  — go to tab N\n"
        "  :tabc  — close current tab"
    ),
    (
        "Yank a section of text in one window, switch to a different "
        "split, and paste it there.",
        "Yank normally (yy, V then y, etc.)\n"
        "  Ctrl-w w  — switch to other split\n"
        "  p  — paste  (the default register is shared across splits/tabs)"
    ),
    (
        "Use a count with a motion to move efficiently — e.g. jump 5 words, "
        "delete 3 lines.",
        "{count}{motion}  e.g.  5w  3dd  2j  4k  6l\n"
        "  Counts work with almost any motion and operator."
    ),
]


ADVANCED = [
    (
        "Run an ex command on every line that matches a pattern — "
        "e.g. delete all lines containing 'TODO'.",
        ":g/pattern/command\n"
        "  :g/TODO/d  — delete all TODO lines\n"
        "  :g/^$/d    — delete all blank lines\n"
        "  :g/pattern/norm dd  — run normal-mode command on matching lines"
    ),
    (
        "Run a normal-mode command on a range of lines — "
        "e.g. comment out lines 5 through 15.",
        ":5,15norm I//  — prepend // to lines 5-15\n"
        "  :%norm A;    — append ; to every line in the file\n"
        "  :'<,'>norm {cmd}  — run on visual selection"
    ),
    (
        "Delete a rectangular block of text (e.g. a column) across multiple lines.",
        "Ctrl-v  — enter block visual mode\n"
        "  Select the block with j/k and h/l\n"
        "  d  or  x  — delete the block"
    ),
    (
        "Insert the same text at the beginning of multiple lines simultaneously "
        "using block visual mode.",
        "Ctrl-v  — block visual\n"
        "  Select lines with j/k\n"
        "  I  — insert before block  (or  A  to append after)\n"
        "  Type text, then Esc  — text appears on all selected lines"
    ),
    (
        "Filter the entire file (or a visual selection) through a shell command — "
        "e.g. sort all lines.",
        ":%!sort   — pipe whole file through sort\n"
        "  :'<,'>!sort  — pipe selection through sort\n"
        "  :%!python3 -m json.tool  — pretty-print JSON"
    ),
    (
        "Insert the output of a shell command into the buffer at the cursor position.",
        ":r !command  — inserts stdout below cursor\n"
        "  :r !date   — inserts current date/time\n"
        "  :r !ls     — inserts directory listing"
    ),
    (
        "Run an ex command across multiple files at once using :argdo.",
        ":args *.py          — load all .py files into the arg list\n"
        "  :argdo %s/old/new/ge | update  — replace in all, save each\n"
        "  :args  — list current arg list"
    ),
    (
        "Open the quickfix list, navigate through entries, and close it.",
        ":copen  — open quickfix window\n"
        "  :cn / :cp  — next / previous entry\n"
        "  :cc{N}  — jump to entry N\n"
        "  :cclose  — close quickfix window\n"
        "  (Populated by :make, :grep, :vimgrep, LSP diagnostics, etc.)"
    ),
    (
        "Search recursively across files using vimgrep and navigate the results.",
        ":vimgrep /pattern/gj **/*.py  — search all .py files\n"
        "  :copen  — see matches in quickfix\n"
        "  :cn / :cp  — jump through matches"
    ),
    (
        "Jump to the definition of a function using a ctags index.",
        "Ctrl-]  — jump to tag under cursor\n"
        "  Ctrl-t  — jump back\n"
        "  :tag {name}  — jump to named tag\n"
        "  :tn / :tp  — next / previous tag match\n"
        "  (Requires a 'tags' file — generate with: ctags -R .)"
    ),
    (
        "Jump to the local declaration of the variable or function name "
        "under the cursor.",
        "gd  — go to local declaration\n"
        "  gD  — go to global declaration\n"
        "  (No tags file required — vim searches the buffer)"
    ),
    (
        "Set a global (cross-file) mark, open a different file, "
        "and jump back to the mark.",
        "mA  — set global mark A (uppercase = global)\n"
        "  `A  — jump back to exact position from any file\n"
        "  'A  — jump to the line of the mark\n"
        "  :marks  — list all marks"
    ),
    (
        "Reformat a paragraph of prose to wrap at a set line width.",
        ":set textwidth=80\n"
        "  gqap  — reformat current paragraph\n"
        "  gq{motion}  — reformat any motion\n"
        "  gqq  — reformat current line"
    ),
    (
        "Enable spell checking, jump to misspelled words, and get correction suggestions.",
        ":set spell  (disable with :set nospell)\n"
        "  ]s  — next misspelling   [s  — previous\n"
        "  z=  — show correction suggestions\n"
        "  zg  — add word to dictionary   zw  — mark word as wrong"
    ),
    (
        "Open a terminal inside neovim and switch back to normal mode from it.",
        ":terminal  or  :term  — open terminal\n"
        "  i or a  — enter terminal-insert mode (to type commands)\n"
        "  Ctrl-\\ Ctrl-n  — exit terminal mode back to normal mode\n"
        "  Treat it like a regular buffer once in normal mode"
    ),
    (
        "Create a fold over a range of lines, then open, close, and toggle it.",
        "zf{motion}  — create a manual fold  (e.g. zf5j)\n"
        "  zo  — open fold   zc  — close fold   za  — toggle\n"
        "  zR  — open ALL folds   zM  — close ALL folds\n"
        "  :set foldmethod=indent  — auto-fold by indentation"
    ),
    (
        "Read an entire file's contents into the current buffer at the cursor.",
        ":r filename  — inserts file contents below current line\n"
        "  :0r filename  — insert at the very top of the buffer"
    ),
    (
        "Use :bufdo to run a substitution across all open buffers and save each.",
        ":bufdo %s/old/new/ge | update\n"
        "  ge  — suppress error if pattern not found in a buffer\n"
        "  update  — save only if buffer was changed"
    ),
    (
        "Apply a macro to every line in a visual selection.",
        "Select lines with V\n"
        "  :norm @a  — runs macro 'a' on each selected line\n"
        "  (:'<,'>norm @a is what vim actually executes)"
    ),
    (
        "Navigate the location list (per-window quickfix) and close it.",
        ":lopen  — open location list\n"
        "  :ln / :lp  — next / previous\n"
        "  :lclose  — close\n"
        "  (LSP populates this independently per window)"
    ),
]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def header():
    print()
    print(BOLD + "=" * 56 + RESET)
    print(BOLD + "   Vim Drills  —  " + datetime.date.today().strftime("%b %d %Y") + RESET)
    print(BOLD + "=" * 56 + RESET)
    print()

def ask_include(level_name):
    ans = input(f"Include {level_name}? [y/n] ").strip().lower()
    return ans == "y"

def separator():
    print(DIM + "-" * 56 + RESET)

def run_drills(exercises):
    random.shuffle(exercises)
    total = len(exercises)

    print()
    print(f"  {total} exercises queued. Press {BOLD}<Enter>{RESET} to reveal the hint,")
    print(f"  {BOLD}<Enter>{RESET} again to advance. Type {BOLD}q{RESET} at any prompt to quit.")
    print()

    for idx, (task, hint) in enumerate(exercises, 1):
        separator()
        print(f"\n  {CYAN}{BOLD}[{idx}/{total}]{RESET}  {BOLD}{task}{RESET}\n")

        raw = input("  > ").strip().lower()
        if raw == "q":
            break

        print()
        print(f"  {YELLOW}Hint:{RESET}")
        for line in hint.split("\n"):
            print(f"    {GREEN}{line}{RESET}")
        print()

        raw = input("  > ").strip().lower()
        if raw == "q":
            break

    else:
        separator()
        print()
        print(f"  {BOLD}{GREEN}All done! Great work.{RESET}")
        print()
        return

    separator()
    print()
    print(f"  {DIM}Session ended at exercise {idx}/{total}.{RESET}")
    print()


def main():
    header()

    pool = []

    if ask_include("Beginner"):
        pool.extend(BEGINNER)
    if ask_include("Intermediate"):
        pool.extend(INTERMEDIATE)
    if ask_include("Advanced"):
        pool.extend(ADVANCED)

    if not pool:
        print("\n  Nothing selected. Goodbye.\n")
        sys.exit(0)

    run_drills(pool)


if __name__ == "__main__":
    main()
