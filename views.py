def product_view(request, slug, template_name="lfs/catalog/product_base.html"):
    """Main view to display a product.
    """
    product = lfs_get_object_or_404(Product, slug=slug)

    if (request.user.is_superuser or product.is_active()) == False:
        raise Http404()

    # Store recent products for later use
    recent = request.session.get("RECENT_PRODUCTS", [])
    if slug in recent:
        recent.remove(slug)
    recent.insert(0, slug)
    if len(recent) > settings.LFS_RECENT_PRODUCTS_LIMIT:
        recent = recent[:settings.LFS_RECENT_PRODUCTS_LIMIT + 1]
    request.session["RECENT_PRODUCTS"] = recent

    if product.is_variant():
        variant_canonical = product.parent.get_variant_for_category(request)
    else:
  variant_canonical = product
	
    result = render_to_response(template_name, RequestContext(request, {
        "product_inline": product_inline(request, product),
        "product": product,
      	"variant_canonical" : variant_canonical,
        "first_category" : product.get_category(),	
    }))

    return result
