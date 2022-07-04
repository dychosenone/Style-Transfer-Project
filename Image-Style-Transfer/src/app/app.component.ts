import {
  trigger,
  state,
  style,
  animate,
  transition,
  // ...
} from '@angular/animations';
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
  

  
  
})
export class AppComponent {
  CurrentPage = 1;
  
  async SetCurrentPage(value: number){
    this.CurrentPage = 0; 
    await new Promise(f => setTimeout(f, 760));
    this.CurrentPage = value;

    console.log('parent: ' + this.CurrentPage);
  }
  
  title = 'Image-Style-Transfer'; 
}
