# lfs imports
from lfs.core.sitemap import CategorySitemap
from lfs.core.sitemap import PageSitemap
from lfs.core.sitemap import ProductSitemap0
#from lfs.core.sitemap import ProductSitemap1
from lfs.core.sitemap import ProductSitemap2
from lfs.core.sitemap import ShopSitemap
from lfs.core.views import one_time_setup

# Robots
urlpatterns = patterns('django.views.generic.simple',
    (r'^robots.txt', 'direct_to_template', {'template': 'lfs/shop/robots.txt'}),
)

# Sitemaps
urlpatterns += patterns("django.contrib.sitemaps.views",
    url(r'^sitemap.xml$', 'sitemap', {'sitemaps': {"products0": ProductSitemap0,"products2": ProductSitemap2, "categories": CategorySitemap, "pages": PageSitemap, "shop": ShopSitemap}})
)
