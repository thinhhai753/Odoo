odoo.define('buttons.VoucherPopup', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const { useState, useRef, onMounted } = owl;


    class VoucherPopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }
    }

    VoucherPopup.template = 'VoucherPopup';
    Registries.Component.add(VoucherPopup);

    // return VoucherPopup
});
