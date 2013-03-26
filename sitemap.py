class ProductSitemap0(Sitemap):
    """Google's XML sitemap for products.
    """
    changefreq = "weekly"
    priority = 0.1

    def items(self):
        return Product.objects.filter(sub_type=0, active='TRUE')
    def lastmod(self, obj):
        return obj.creation_date

class ProductSitemap2(Sitemap):
    """Google's XML sitemap for products.
    """
    changefreq = "yearly"
    priority = 0.1

    def items(self):
        return Product.objects.filter(sub_type=2, active='TRUE')
    def lastmod(self, obj):
        return obj.creation_date

class CategorySitemap(Sitemap):
    """Google's XML sitemap for products.
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.creation_date
