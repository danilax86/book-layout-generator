import unittest

from app import PageBlock, book_layout


class TestBookLayout(unittest.TestCase):

    def test_book_layout_even_number_of_blocks(self):
        page_blocks = [
            PageBlock(10, 20),
            PageBlock(30, 40),
            PageBlock(50, 60),
            PageBlock(70, 80)
        ]

        result = book_layout(page_blocks)

        expected_result = [
            PageBlock(10, 80),
            PageBlock(30, 60),
            PageBlock(50, 40),
            PageBlock(70, 20)
        ]
        self.assertEqual(result, expected_result)

    def test_book_layout_odd_number_of_blocks(self):
        page_blocks = [
            PageBlock(10, 20),
            PageBlock(30, 40),
            PageBlock(50, 60)
        ]

        result = book_layout(page_blocks)

        expected_result = [
            PageBlock(10, 60),
            PageBlock(30, 40),
            PageBlock(50, 20)
        ]
        self.assertEqual(result, expected_result)

    def test_book_layout_single_block(self):
        page_blocks = [
            PageBlock(10, 20)
        ]

        result = book_layout(page_blocks)

        expected_result = [
            PageBlock(10, 20)
        ]
        self.assertEqual(result, expected_result)

    def test_book_layout_empty_list(self):
        page_blocks = []

        result = book_layout(page_blocks)

        expected_result = []
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
