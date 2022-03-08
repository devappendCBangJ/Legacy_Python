"""
● Linux
    1. file editor : vi filename
        1) command mode : ESC
            (1) write : : w filename
            (2) 1word erase : x
            (2) 1line erase : dd
            (2) nline erase : d1 or d2 ...

            (3) 1line back + 1word append : a
            (3) 1line back + 1line append : o

            (4) cw : 1word replace
            (4) r : 1word replace

            (5) 1line copy : Y
            (5) nline copy : Y1 or Y2...
            (5) paste : P

            (6) exit : :q
            (6) force exit : :q!
            (6) keep : Ctrl + z
        2) input mode : i
    2. workspace save & load
    	1) file foreground(previous work) : fg
	    2) current state save : pushd .
	    2) previous state load : pop .
	3. file control
		1) file copy(file1 -> file2) : cp file1.extension file2.extension
		2) file copy(file1 -> dir1) : cp file1.extension dir1/
		3) multi-file copy(file1, file2, ... -> dir1) : cp file1.extension file2.extension dir1/
		4) dir copy(dir1 -> dir2) : cp -r dir1/ dir2/
"""
