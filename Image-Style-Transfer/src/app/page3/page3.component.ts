import {
    trigger,
    state,
    style,
    animate,
    transition,
    // ...
    } from '@angular/animations';
import { Component, NgModule, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
    selector: 'page-3',
    templateUrl: './page3.component.html',
    styleUrls: ['./page3.component.css'],
    animations:[
        trigger("InOutAnimation", [
            transition(":enter", [
                style({ opacity: 0 }), //apply default styles before animation starts
                animate(
                    "750ms ease-in-out",
                    style({ opacity: 1})
                )
            ]),
            transition(":leave", [
                style({ opacity: 1}), //apply default styles before animation starts
                animate(
                    "750ms ease-in-out",
                    style({ opacity: 0})
                )
            ])
        ]),

        trigger("GenerateBtn", [
            transition(":enter", [
                style({opacity: 0}), animate("750ms", style({opacity: 1}))
            ])
        ])
    ]
})

export class page3Component{
    @Output() newPageEvent = new EventEmitter<number>();

    @Input() CurrentPage = -1;
  
    SetCurrentPage(value: number){
      this.newPageEvent.emit(value);
  
      console.log('page 3: ' + this.CurrentPage);
    }

}