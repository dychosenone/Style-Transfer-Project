import { Component } from '@angular/core';
import {
  trigger,
  state,
  style,
  animate,
  transition,
  // ...
} from '@angular/animations';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
    // animation triggers go here
    trigger('openClose_Page1', [
      state('open', style({
        opacity: '1'
      })),
      state('close', style({
        opacity: '0'
      })),
      transition('open => closed', [animate('5s')])
      
    ])
  ]
})
export class AppComponent {
  title = 'Image-Style-Transfer';
  Page1_Status: String = 'open';
  
  Trigger(page: any){
    switch (page){
      case 1:
        this.Page1_Status = this.Page1_Status == 'open' ? 'close' : 'open';
        break;
    }
      
  }
}
