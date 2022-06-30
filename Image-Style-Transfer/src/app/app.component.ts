import { Component, ViewEncapsulation } from '@angular/core';
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
    trigger("inOutPaneAnimation", [
      transition(":enter", [
        style({ opacity: 0}), //apply default styles before animation starts
        animate(
          "500ms ease-in-out",
          style({ opacity: 1})
        )
      ]),
      transition(":leave", [
        style({ opacity: 1}), //apply default styles before animation starts
        animate(
          "500ms ease-in-out",
          style({ opacity: 0})
        )
      ])
    ])
  ],
})
export class AppComponent {
  title = 'Image-Style-Transfer';
  Page1_Display = true;
  Page2_Display = false;

  async delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
  }

  async Start(){
    this.Page1_Display = !this.Page1_Display;
    await this.delay(510);
    this.Page2_Display = !this.Page2_Display;
  }

  
}
