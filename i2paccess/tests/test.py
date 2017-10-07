from django.test import TestCase, override_settings

TEST_SETTINGS = {
    "whitelist": ["choosenone1pgcujqsk22hpxgyq3t6gjnu4wcu6cqagtame2spoq"],
    "blacklist": ["bob6d4psz73qurfnzv2tivotzxx63nylwdvsxrywpemxqedzk4wa"],
    "regex": "bob",
}

WHITELISTED_B32 = "choosenone1pgcujqsk22hpxgyq3t6gjnu4wcu6cqagtame2spoq.b32.i2p"
REGEX_B32       = "bobxtayesmvf2422vt24rm2hquh3f7m7xzideqjstckcvt2aelba.b32.i2p"
RANDOM_B32      = "randd4psz73qurfnzv2tivotzxx63nylwdvsxrywpemxqedzk4wa.b32.i2p"
BLACKLISTED_B32 = "bob6d4psz73qurfnzv2tivotzxx63nylwdvsxrywpemxqedzk4wa.b32.i2p"

@override_settings(I2P_ACCESSLIST=TEST_SETTINGS)
@override_settings(ROOT_URLCONF='i2paccess.tests.urls')
class I2PAccessTestCase(TestCase):

    def test_decorator_whitelist_success(self):
        headers = {'HTTP_X_I2P_DESTB32': WHITELISTED_B32}
        resp = self.client.get("/secretview/", **headers)
        self.assertEqual(resp.status_code, 200)

    def test_decorator_regex_success(self):
        headers = {'HTTP_X_I2P_DESTB32': REGEX_B32}
        resp = self.client.get("/secretview/", **headers)
        self.assertEqual(resp.status_code, 200)

    def test_decorator_fail(self):
        headers = {'HTTP_X_I2P_DESTB32': RANDOM_B32}
        resp = self.client.get("/secretview/", **headers)
        self.assertEqual(resp.status_code, 403)
        
    def test_decorator_blacklist_fail(self):
        headers = {'HTTP_X_I2P_DESTB32': BLACKLISTED_B32}
        resp = self.client.get("/secretview/", **headers)
        self.assertEqual(resp.status_code, 403)

    # middleware tests
    def test_middleware_whitelist_success(self):
        headers = {'HTTP_X_I2P_DESTB32': WHITELISTED_B32}
        resp = self.client.get("/secretclassview/", **headers)
        self.assertEqual(resp.status_code, 200)

    def test_middleware_regex_success(self):
        headers = {'HTTP_X_I2P_DESTB32': REGEX_B32}
        resp = self.client.get("/secretclassview/", **headers)
        self.assertEqual(resp.status_code, 200)

    def test_middleware_fail(self):
        headers = {'HTTP_X_I2P_DESTB32': RANDOM_B32}
        resp = self.client.get("/secretclassview/", **headers)
        self.assertEqual(resp.status_code, 403)
        
    def test_middleware_blacklist_fail(self):
        headers = {'HTTP_X_I2P_DESTB32': BLACKLISTED_B32}
        resp = self.client.get("/secretclassview/", **headers)
        self.assertEqual(resp.status_code, 403)
