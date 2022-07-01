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
    selector: 'page-1',
    templateUrl: './page1.component.html',
    styleUrls: ['./page1.component.css'],
    animations:[
      trigger("InOutAnimation", [
        transition(":enter", [
            style({ opacity: 0}), //apply default styles before animation starts
            animate(
                "750ms ease-in-out",
                style({ opacity: 1})
            )
        ]),
        transition(":leave", [
            style({ opacity: 1, transform: "translateX(0)" }), //apply default styles before animation starts
            animate(
                "750ms ease-in-out",
                style({ opacity: 0, transform: "translateX(-100%)" })
            )
        ])
      ])
    ]
})


export class page1Component{
  @Output() newPageEvent = new EventEmitter<number>();

  @Input() CurrentPage = -1;

  async SetCurrentPage(value: number){
    this.newPageEvent.emit(value);

    
    
    console.log('page 1: ' + this.CurrentPage);
  }

  

}