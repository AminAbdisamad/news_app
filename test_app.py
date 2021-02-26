# import unittest


# class TestApp(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(sum([2,6]),8,'Should be 8')


# if __name__ == '__main__':
#     unittest.main()


"""
<form action="{{ url_for('dashboard.delete_post',id=post.id) }}" method="post">
            <input  type="submit" value="Delete" onclick="return confirm('Are you sure?');">
</form>
"""
from datetime import datetime

print(datetime.now())
