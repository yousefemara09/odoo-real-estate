/* @odoo-module */

import { Component , useState , onWillUnmount} from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks"; /* ده الـ Base Class اللى أى OWL Component بيرث منه. */

import { FormViewAction as FormView } from "@app_one/componants/formView/formView"

export class ListViewAction extends Component {
    static template = "app_one.ListView";
    static components = {FormView}
    setup() {
    /*private attribute*/
    this.state = useState({
        'records':[],
    })
    this.orm = useService("orm")
    this.rpc = useService("rpc")
    this.loadRecords();
//    this.loadRecords();
    this.onRecordCreated = this.onRecordCreated.bind(this);
    this.intervalId = setInterval( ()=>{
       this.loadRecords();
    } ,3000);
    onWillUnmount( ()=>{
        clearInterval(this.intervalId)
    })

    };
//     async loadRecords(){
//        const result = await this.orm.searchRead("property", [] , []);
//        console.log(result)
//        this.state.records = result;
//     };
     async loadRecords() {
            const result = await this.rpc("/web/dataset/call_kw", {
                   model: "property",
                   method: "search_read",
                   args: [[]],
                   kwargs: {
                   fields: ["name", "postcode", "bedrooms", "garden"],
                   },
     });

        console.log(result);
        this.state.records = result;
    }
     async createRecords(){
        await this.rpc("/web/dataset/call_kw",{
            model:"property",
            method:"create",
            args:[[{
                name:"property_new_2",
                postcode :"P0003",
                expected_price :887488,
                bedrooms :16,

            }]],
            kwargs:{},
        })
        this.loadRecords();
     };

     async deleteRecords(recordId){
        await this.rpc("/web/dataset/call_kw",{
            model:"property",
            method:"unlink",
            args:[[recordId]],
            kwargs:{},
        })
        this.loadRecords();
     };

     toggleCreateForm(){
        console.log("inside toggle create fom method");
        this.state.showCreateform = !this.state.showCreateform;
        console.log(this.state.showCreateform)
     };

     onRecordCreated(){
         this.loadRecords();
         this.state.showCreateform = false;

     };

}
registry.category("actions").add("app_one.action_list_view", ListViewAction);


