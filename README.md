SEO
===

To improve SEO in LFS, I suggest :
1)Avoid having all the product twice in SE index : robots.txt

2)Canonical all variant of the multi variant product on the variant of the method "parent.get_variant_for_category".
Offer to admin ability for select some categories which have all the product Canonical to the category. I used 'level' field of category which seam to be useless, but a boolean field 'canonical' would be better :
product_base.html

3) Improve Sitmap.py :
Add a field 'creation_date' in class category idem as in product in the catalog model and return this creation_date idem in the class sitemap for category.
Append to  "return Product.objects.filter(active='TRUE')"  "exclude(sub_type=1)" in order to concentrate sitemap to useful product.
TODO have a Class with sub_type=1 and another one with :
sub-type=2 and product = product.parent.get_variant_for_category, but Django can't use a method in a filter and I didn't find an elegant solution.
sitemap.py and urls.py

4) Use Rich snippets, look at google doc and : product_inline.html. You can add other itemprop of schema.org/Product.
and breadcrumbs.html.

5) Canonical pages to the category slug : in the category_view in views.py add in the render to response (line 281) : "pagination":request.REQUEST.get("start", 0), . In category_base.html, add in the block head : {% if pagination != 0 %}
{% endif %}.

Pierre
