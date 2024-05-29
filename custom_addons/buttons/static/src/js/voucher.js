odoo.define('buttons.VoucherButton', function (require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');
    const { isConnectionError } = require('point_of_sale.utils');

    class VoucherButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener("click", this.onClick);
        
          }
          async onClick() {
            try {
                // Fetch voucher data from the server
                const vouchers = await this.rpc({
                    model: 'coupon.program',
                    method: 'search_read',
                    args: [[], ['name', 'promo_code', 'rule_date_from', 'rule_date_to', 'maximum_use_number','pos_order_count']],
                });
                // Show the popup with the voucher data
                this.showPopup('VoucherPopup', { 
                    title: 'Voucher List',
                    vouchers: vouchers,
                });
            } catch (error) {
                console.error('Error:', error);
                this.showPopup('ErrorPopup', {
                    title: this.env._t('Network Error'),
                    body: this.env._t('Cannot access voucher list if offline.'),
                });
            }
        }
    }
    VoucherButton.template = 'VoucherButton';
    

    ProductScreen.addControlButton({
        component: VoucherButton,
        condition: function () {
            return true;
        },
    });

    Registries.Component.add(VoucherButton);

    return VoucherButton;
});
