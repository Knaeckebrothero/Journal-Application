import { Component } from '@angular/core';
import { NavigationBarService } from '../navbar/navigation-bar.service';

@Component({
  selector: 'app-activities',
  templateUrl: './landingpage.component.html',
  styleUrls: ['./landingpage.component.scss']
})
export class ActivitiesComponent {
  constructor(private navService: NavigationBarService) { }

  toggleNavbar() {
    this.navService.toggleSidenav();
  }
}
