#!/usr/bin/python3
"""prevents the user from dynamically creating new instance"""


class LockedClass:
    """prevents the user from dynamically creating new instance"""

    def __setattr__(self, name, value):
        """prevents the user from dynamically creating new instance"""

        if name != 'first_name':
            raise AttributeError(
                    f"'{type(self).__name__}' object has no attribute '{name}'"
            )
        super().__setattr__(name, value)
