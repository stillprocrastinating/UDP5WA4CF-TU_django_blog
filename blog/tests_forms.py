from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Docstring for TestCommentForm
    """

    def test_form_is_valid(self):
        """
        Docstring for test_form_is_valid
        
        :param self: Description
        """

        comment_form = CommentForm({
            'body': 'This is a great post'
        })
        self.assertTrue(
            comment_form.is_valid(),
            msg='Form is invalid'
        )

    def test_form_is_invalid(self):
        """
        Docstring for test_form_is_invalid
        
        :param self: Description
        """
        
        comment_form = CommentForm({
            'body': ''
        })
        self.assertFalse(
            comment_form.is_valid(),
            msg='Form is valid'
        )
