import pytest
from task_02_verboselist import VerboseList
"""
Test Module for VerboseList notification system.

Tests include:
    - append notification "Added [item] to the list."
    - extend notification "Extended the list with [x] items."
    - remove notification "Removed [item] from the list."
    - pop notification    "Popped [item] from the list."
"""

class TestClass:
    def test_verbose_list(self):
        vb = VerboseList()
        assert isinstance(vb, VerboseList) == True

    def test_append_notification(self, capfd):
        vb = VerboseList()
        vb.append(1)
        out, err = capfd.readouterr()
        assert out == "Added [1] to the list.\n"
    
    def test_extend_notification(self, capfd):
        vb = VerboseList()
        extendme = [1, 2, 3]
        vb.extend(extendme)
        out, err = capfd.readouterr()
        assert out == "Extended the list with [3] items.\n"

    def test_remove_notification(self, capfd):
        vb = VerboseList()
        vb.append(3)
        vb.append(1)
        vb.remove(3)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "Removed [3] from the list."
        assert vb == [1]

    def test_remove_non_existant(self):
        with pytest.raises(ValueError):
            vb = VerboseList()
            vb.remove(200)

    def test_pop_notification(self, capfd):
        vb = VerboseList()
        vb.append(3)
        vb.append(1)
        num = vb.pop(1)
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "Popped [1] from the list."
        assert vb == [3]
        assert num == 1
        num = vb.pop()
        assert num == 3

    def test_pop_non_existant(self):
        with pytest.raises(IndexError):
            vb = VerboseList()
            vb.pop(200)
