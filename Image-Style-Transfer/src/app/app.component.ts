import { Component, ViewEncapsulation } from '@angular/core';
import {
  trigger,
  state,
  style,
  animate,
  transition,
  // ...
} from '@angular/animations';
import { SafeUrl, DomSanitizer } from "@angular/platform-browser";

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
    ]),

    trigger("slide_animation", [
      transition(":enter", [
        style({ opacity: 0, transform: "translateY(-100%)"}), //apply default styles before animation starts
        animate(
          "500ms ease-in-out",
          style({ opacity: 1, transform: "translateY(0%)"})
        )
      ]),
      transition(":leave", [
        style({ opacity: 1, transform: "translateY(0%)"}), //apply default styles before animation starts
        animate(
          "500ms ease-in-out",
          style({ opacity: 0, transform: "translateY(-100%)"})
        )
      ])
    ]),

    
  ],
})
export class AppComponent {
  title = 'Image-Style-Transfer';
  Page1_Display = true;
  Page2_Display = false;

  Page2_Content_Display = false;
  Page2_Style_Display = false;

  contentImage: any = "assets/images/imageicon.png"
  styleImage: any = "assets/images/imageicon.png"

  constructor(private sanitizer: DomSanitizer) {}

  updateImage(ev: any, type: string){
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
  }

  async Start(){
    this.Page1_Display = !this.Page1_Display;
    await new Promise(f => setTimeout(f, 510));
    this.Page2_Display = !this.Page2_Display;

    await new Promise(f => setTimeout(f, 510));

    this.Page2_Content_Display = !this.Page2_Content_Display;    
    await new Promise(f => setTimeout(f, 210)); 
    this.Page2_Style_Display = !this.Page2_Style_Display;  
  }


  async Back(){
    this.Page2_Content_Display = !this.Page2_Content_Display;   
    await new Promise(f => setTimeout(f, 210)); 
    this.Page2_Style_Display = !this.Page2_Style_Display;  

    await new Promise(f => setTimeout(f, 510));

    this.Page2_Display = !this.Page2_Display;
    await new Promise(f => setTimeout(f, 510));

    this.Page1_Display = !this.Page1_Display;
  }

  
}
