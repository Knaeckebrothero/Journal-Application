// Components
import { NavigationBarComponent } from './navbar/navigation-bar.component';
import { ActivitiesComponent } from './activities/activities.component';

// Base
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { RouterModule, Routes } from '@angular/router';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { RateComponent } from './rate/rate.component';
import { HeadBarComponent } from './head-bar/head-bar.component';
import {MatIconModule} from '@angular/material/icon';


// Routes
const routes: Routes = [
  { path: 'activities', component: ActivitiesComponent },
  { path: 'rate', component: RateComponent },
  //{ path: 'comment', component: CommentComponent }
  { path: '', redirectTo: 'activities', pathMatch: 'full' }
];

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    ActivitiesComponent,
    RateComponent,
    HeadBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule,
    RouterModule.forRoot(routes),
    ServiceWorkerModule.register('ngsw-worker.js', {
      registrationStrategy: 'registerWhenStable'
    }),
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
