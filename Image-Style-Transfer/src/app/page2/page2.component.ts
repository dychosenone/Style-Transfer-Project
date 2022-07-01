import {
trigger,
state,
style,
animate,
transition,
// ...
} from '@angular/animations';
import { Component, NgModule, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { SafeUrl, DomSanitizer } from "@angular/platform-browser";

@Component({
    selector: 'page-2',
    templateUrl: './page2.component.html',
    styleUrls: ['./page2.component.css'],
    animations:[
        trigger("InOutAnimation", [
            transition(":enter", [
                style({ opacity: 0, transform: "translateX(100%)" }), //apply default styles before animation starts
                animate(
                    "750ms ease-in-out",
                    style({ opacity: 1, transform: "translateX(0)" })
                )
            ]),
            transition(":leave", [
                style({ opacity: 1, transform: "translateX(0)" }), //apply default styles before animation starts
                animate(
                    "750ms ease-in-out",
                    style({ opacity: 0, transform: "translateX(100%)" })
                )
            ])
        ]),

        trigger("GenerateBtn", [
            
        ])
    ]
})


export class page2Component{

    contentImage: any = "assets/images/imageicon.png"
    styleImage: any = "assets/images/imageicon.png"

    GenerateBtn_Display = false;

    @Output() newPageEvent = new EventEmitter<number>();

    @Input() CurrentPage = -1;
  
    SetCurrentPage(value: number){
      this.newPageEvent.emit(value);
  
      console.log('page 2: ' + this.CurrentPage);
    }

    constructor(private sanitizer: DomSanitizer) {}

    UpdateImage(ev: any, type: string){
        if(type == "content"){
        this.contentImage = this.sanitizer.bypassSecurityTrustUrl(
            window.URL.createObjectURL(ev.target.files[0])
        );
        }

        if (type == "style"){
        this.styleImage = this.sanitizer.bypassSecurityTrustUrl(
            window.URL.createObjectURL(ev.target.files[0])
        );
        }

        if(this.contentImage != "assets/images/imageicon.png" && this.styleImage != "assets/images/imageicon.png"){
        this.GenerateBtn_Display = true;
        }
    }
}