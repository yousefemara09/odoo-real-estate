/* @odoo-module */
import { Component , useState , onWillUnmount} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

export class FormViewAction extends Component {
    static template = "app_one.formView";
    setup(){
        this.state = useState({
            name:"",
            postcode:"",
            expected_price:""
        })
        this.rpc = useService("rpc")
    }

    async createRecords(){
        await this.rpc("/web/dataset/call_kw",{
            model:"property",
            method:"create",
            args:[{
                 name : this.state.name,
                 postcode : this.state.postcode,
                 expected_price : this.state.expected_price,
            }],
            kwargs:{},
            })
        this.props.onRecordCreated();
     };

    cancel(){
        this.state.name = "";
        this.state.postcode = "";
        this.state.expected_price = "";
        this.props.onCancle();
    }


}
