from django.test import TestCase, Client


def extract_uid(v):
    return v.split("My unique ID is: ")[1].split(".")[0]


class TestRoot(TestCase):
    def test_root(self):
        c = Client()

        v = extract_uid(c.get("/").rendered_content)
        self.assertEquals(len(v), 36)

        w = extract_uid(c.get("/").rendered_content)
        self.assertEquals(len(w), 36)

        self.assertNotEquals(v, w)
