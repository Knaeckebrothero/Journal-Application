import { NgModule, isDevMode } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ServiceWorkerModule } from '@angular/service-worker';

import { RouterModule, Routes } from '@angular/router';
import { ActivitiesComponent } from './activities/activities.component';
import { NavigationBarComponent } from './navbar/navigation-bar.component';
import { HeadBarComponent } from './head-bar/head-bar.component';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { RateComponent } from './rate/rate.component';
import { CommentComponent } from './comment/comment.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

// Routes
const routes: Routes = [
  { path: 'activities', component: ActivitiesComponent },
  { path: 'rate', component: RateComponent },
  { path: 'comment', component: CommentComponent },
  { path: '', redirectTo: '/activities', pathMatch: 'full' }
];

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    ActivitiesComponent,
    HeadBarComponent,
    RateComponent,
    CommentComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatListModule,
    MatIconModule,
    RouterModule.forRoot(routes),
    ServiceWorkerModule.register('ngsw-worker.js', {
      enabled: !isDevMode(),
      // Register the ServiceWorker as soon as the application is stable
      // or after 30 seconds (whichever comes first).
      registrationStrategy: 'registerWhenStable:30000'
    }),
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
