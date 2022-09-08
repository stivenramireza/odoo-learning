odoo.define('custom_item.action_button', function (require) {
	"use strict";
	var core = require('web.core');
	var ListController = require('web.ListController');
	var rpc = require('web.rpc');
	var session = require('web.session');
	var _t = core._t;
	ListController.include({
		renderButtons: function ($node) {
			this._super.apply(this, arguments);
			if (this.$buttons) {
				this.$buttons.find('.oe_action_button').click(this.proxy('action_def'));
			}
		},
		action_def: function(){
		    var self = this
		    var user = session.uid;
		    rpc.query(
		        {
		        model: 'odoo_view_advanced.custom_item',
		        method: 'remove_items',
		        args: [
		            [user], {
		                'id': user
		            }
		        ]
		        }
		    ).then(function (e) {
                self.do_action({
                    name: _t('action_custom_item'),
                    type: 'ir.actions.act_window',
                    res_model: 'odoo_view_advanced.custom_item',
                    views: [[false, 'form']],
                    view_mode: 'form',
                    target: 'new',
                });
                window.location
            });
		}
	})
});