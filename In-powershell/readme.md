# In this file we will do the following-
# 1.run python using powershell.
- powershell is used to run a piece of code inside the python idle.

        open in integrated terminal and then type python.
        -- we can import the file inside using command -
                    import _file-name
                    -now we can use the file methods and attributes.

    2.NOTE- when we import a file in python idle and after we do some changes in that and then we want the changes in our current running powershell so we face some error to fix that we have two options

        A-close the terminal and then open it again and import the file again.

        B- Smarter way --
            -- import the reload method from importlib(its use to reload the file and get the current changes)
            using -- from importlib import reload
            and then run -- reload(<file-name>)
            now you can get the current changes in your current powershell.