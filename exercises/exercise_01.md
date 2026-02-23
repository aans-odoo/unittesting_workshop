
# Exercise 01

## Statement -
  Write two tests on a product:
    1. Verify that when you create a product with listing price, the listing
       price field is stored correctly.
    2. Verify that when you add some tag on a product, the tag is correctly
       linked to that product.

## Helpers -
  To create a product you can use:
    ```
    # product with listing price
    product = self.env['product.product'].create({
        'name': 'Test Product',
        'list_price': 99.0,
    })

    # product with tags
    product = self.env['product.product'].create({
        'name': 'Test Product 2',
        'list_price': 110.0,
        'product_tag_ids': [Command.create({'name': 'my-tag'})],
    })
    ```

  Tip:
  use 'TransactionCase' to create your test class -
  `from odoo.tests.common import TransactionCase`
